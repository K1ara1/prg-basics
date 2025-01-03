class TV():
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channels = []
      self.volume = 0
   def decrease_volume(self):
        self.volume -= 1
   def increase_volume(self):
       self.volume += 1
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def show_status(self):
        if self.is_on:
            if self.channels:
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]})")
            else:
                print("TV is on, but no channels are set.")
            if 100 >= self.volume >=0:
                print(f"TV volume is set to {self.volume}.")
            else:
                print("You cannot increase or decrease the volume beyond the specified range")
        else:
            print("TV is off")
   def set_channel(self, new_channel_no):
        if 1 <= new_channel_no <= len(self.channels):
                self.channel_no = new_channel_no
        else:
            print("Invalid channel number.")
   def show_channels(self):
        if not self.channels:
            print("No channels available. Please set the channels.")
        else:
            print("Channel list:")
            for idx, channel in enumerate(self.channels, start=1):
                print(f"{idx}. {channel}")
   def set_channels(self, channels_list):
       self.channels = channels_list
        