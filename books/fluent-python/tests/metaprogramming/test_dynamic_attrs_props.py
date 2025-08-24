"""
Unit test of dynamic attributes and properties.

dynamic attributes: present same interface as data attributes, `obj.attr`, but are computed on demand. 
- @property
- __getattr__: virtual attribute

computed properties
- @cached_property: create non-overriding descriptor
- stacking @property @cache

property for attribute validation
- @xxx.setter, __xxx

property(fget=None, fset=None, fdel=None, doc=None) # a class
- are class attributes

property factory
- __dict__, property

attribute deletion
- @xxx.deleter

attribute handling attributes and functions
- __class__, __dict__, __slots__
- dir(), getattr(), setattr(), hasattr(), vars()
- __delattr__(), __dir__(), __getattr__(), __getattribute__(), __setattr__()
"""
# pylint: skip-file

import unittest

JSON_FILE_PATH: str = 'tests/metaprogramming/osconfeed.json'


class TestDynamicAttribute(unittest.TestCase):
  def test_json_osconfeed(self) -> None:
    import json
    with open(JSON_FILE_PATH) as f:
      feed = json.load(f)
    schedule = feed['Schedule']
    print(sorted(schedule.keys()))
    for k, v in schedule.items():
      print(f'{k:>15}: {len(v):3} items')
    for key in schedule.keys():
      print(key)
      for k in schedule[key][0].keys():
        print(f'\t{k}')

  # ['conferences', 'events', 'speakers', 'venues']
  #     conferences:   1 items
  #          events: 484 items
  #        speakers: 357 items
  #          venues:  53 items
  # conferences
  #         serial
  # events
  #         serial
  #         name
  #         event_type
  #         time_start
  #         time_stop
  #         venue_serial
  #         description
  #         website_url
  #         speakers
  #         categories
  # speakers
  #         serial
  #         name
  #         photo
  #         url
  #         position
  #         affiliation
  #         twitter
  #         bio
  # venues
  #         serial
  #         name
  #         category

  def test_json_attributes(self) -> None:
    import json
    from src.metaprogramming.osconfeed import FrozenJSON
    with open(JSON_FILE_PATH) as f:
      raw_feed = json.load(f)
    feed = FrozenJSON(raw_feed)
    self.assertSetEqual({'Schedule'}, set(feed.keys()))
    self.assertListEqual(['conferences', 'events', 'speakers', 'venues'],
                         sorted(feed.Schedule.keys()))
    talk = feed.Schedule.events[0]
    self.assertIsInstance(talk, FrozenJSON)
    with self.assertRaises(KeyError) as cm:
      talk.flavor
    self.assertEqual("'flavor'", str(cm.exception))

  # computed properties

  def test_data_driven_attribute_creation(self) -> None:
    from src.metaprogramming.osconfeed import load, Record
    records = load()
    speaker3471 = records['speaker.3471']
    self.assertIsInstance(speaker3471, Record)
    self.assertEqual('Anna Martelli Ravenscroft',
                     speaker3471.name)  # type: ignore[attr-defined]

  def test_property_to_retrieve_linked_record(self) -> None:
    from src.metaprogramming.osconfeed import Record, Event
    event33950 = Record.fetch('event.33950')
    self.assertIsInstance(event33950, Event)
    venue = event33950.venue  # type: ignore[attr-defined]
    self.assertIsInstance(venue, Record)
    # autopep8: off
    self.assertEqual(1449, event33950.venue_serial) # type: ignore[attr-defined]
    # autopep8: on
    self.assertEqual(1449, venue.serial)

    speakers = event33950.speakers  # type: ignore[attr-defined]
    self.assertListEqual([3471, 5199],
                         [speaker.serial for speaker in speakers])


class TestAttributeValidation(unittest.TestCase):
  def test_lineitem(self) -> None:
    from src.metaprogramming.prop_validate import LineItem
    with self.assertRaises(ValueError) as cm:
      walnuts = LineItem('walnuts', 0, 10.00)
    self.assertEqual('value must be > 0', str(cm.exception))


class TestPropertyFactory(unittest.TestCase):
  def test_lineitem(self) -> None:
    from src.metaprogramming.prop_factory import LineItem
    with self.assertRaises(ValueError) as cm:
      walnuts = LineItem('walnuts', 0, 10.00)
    self.assertEqual('value must be > 0', str(cm.exception))


class TestAttributeDeletion(unittest.TestCase):
  def test_knight(self) -> None:
    from src.metaprogramming.prop_del import BlackKnight
    knight = BlackKnight()
    print(f'next member is: {knight.member}')
    del knight.member
    del knight.member
    del knight.member
    del knight.member
    del knight.member

    # next member is: an arm
    # BLACK KNIGHT (loses an arm) -- 'Tis but a scratch.
    # BLACK KNIGHT (loses another arm) -- It's just a flesh wound.
    # BLACK KNIGHT (loses a leg) -- I'm invincible!
    # BLACK KNIGHT (loses another leg) -- All right, we'll call it a draw.
