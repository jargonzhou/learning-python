"""
Example of attribute deletion.
"""


class BlackKnight:
  def __init__(self) -> None:
    self.phrases = [
        ('an arm', "'Tis but a scratch."),
        ('another arm', "It's just a flesh wound."),
        ('a leg', "I'm invincible!"),
        ('another leg', "All right, we'll call it a draw.")
    ]

  @property
  def member(self) -> str:
    """member"""
    return self.phrases[0][0]

  @member.deleter
  def member(self) -> None:
    if len(self.phrases) > 0:
      member, text = self.phrases.pop(0)
      print(f'BLACK KNIGHT (loses {member}) -- {text}')
    else:
      pass
