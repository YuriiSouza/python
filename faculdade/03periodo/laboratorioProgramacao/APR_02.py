def convertSeconds(seconds):
  
  hour = seconds // 3600
  seconds = seconds % 3600
  minutes = seconds // 60
  seconds = seconds % 60

  time = {'hour': hour,
          'minutes': minutes,
          'seconds': seconds}

  return time


def main():
  a = int(input("seconds: "))
  time = convertSeconds(a)
  print(time)

if __name__ == '__main__':
    main()
    