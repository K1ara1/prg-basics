from tv import TV

def main():
   my_tv = TV()
   my_tv.show_status()
   my_tv.turn_on()
   my_tv.show_status()
   my_tv.show_channels()
   my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
   my_tv.show_channels()
   my_tv.set_channel(5)
   my_tv.show_status()
   my_tv.set_channel(1)
   my_tv.show_status()
   my_tv.set_channel(4)
   my_tv.show_status()
   my_tv.set_channel(2)
   my_tv.show_status()
   my_tv.increase_volume()
   my_tv.show_status()
   my_tv.decrease_volume()
   my_tv.show_status()
   my_tv.turn_off()
   my_tv.show_status()

if __name__ == "__main__":
   main() 