print 'This code is meant to test whether or not you should eat in the classrooms'

a=str(raw_input('is it rainy day schedule'))
while True:
      if a=='yes':
            print 'You may eat in room 3 or 4'
            break
      elif a=='no':
            b=str(raw_input('Are you having a meeting with a teacher?'))
            if b=='yes':
                  print 'You may eat in any room with permission from a teacher'
                  break
            elif b=='no':
                  c=str(raw_input('is it after 5:00 PM?'))
                  if c=='yes':
                      print 'You should be by the main office!'
                      break
                  elif c=='no':
                      print 'You may not eat in any classroom!'
                      break
                  else:
                        print 'Please answer yes or no'
            else:
                  print 'Please answer yes or no'
      else:
            print 'Please answer yes or no'
            a=str(raw_input('is it rainy day schedule'))
