from collections import deque
import pyautogui
import time
import win32api, win32con
import keyboard
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

"""
    Table 1 - Table 2
         Table 3
    Table 4 - Table 5    
"""


def main():
    if pyautogui.pixel(1342, 109) == (254, 203, 0):
        print("We are at start screen")
        start_game()
        wait_until_round_starts()

        if pyautogui.pixel(186, 73)[0] == 151:
            print("in middle of round on stage 1")
            play_stage_1()
            play_stage_2()
            play_stage_3()

        elif pyautogui.pixel(1342, 69) == (255, 155, 8):
            print("We are in middle of round on stage 2")
            play_stage_2()
            play_stage_3()

 #       elif pyautogui.pixel(1342, 69) == (201, 186, 177):
        else:
            print("We are in middle of round on stage 3")
            play_stage_3()

    if pyautogui.pixel(186, 73)[0] == 151:
        print("in middle of round on stage 1")
        play_stage_1()
        play_stage_2()
        play_stage_3()

    elif pyautogui.pixel(1342, 69) == (255, 155, 8):
        print("We are in middle of round on stage 2")
        play_stage_2()
        play_stage_3()

    else:
        print("We are in middle of round on stage 3")
        play_stage_3()


def play_stage_1(): #game playing function
    table_tracker = [True, True, True, True, True] #True means table is available
    table_ordered_tracker = [False, False, False, False, False]
    order_queue = deque([])
    round_is_going = True
    current_balance_image = pyautogui.screenshot('zero_dollars.png', region=(1613, 941, 117, 37))

    while round_is_going and not keyboard.is_pressed('q'):
        penguins_are_waiting = check_if_penguin_waiting()
        if penguins_are_waiting and any(table_tracker):
            table_tracker = seat_waiting_penguin(table_tracker)
        table_ordered_tracker, order_queue = check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue, table_tracker)
        order_queue = check_if_food_plate_ready(order_queue)
        table_tracker, table_ordered_tracker, current_balance = check_if_money_on_any_tables(table_tracker, table_ordered_tracker, current_balance_image)

        if pyautogui.pixel(1732, 515) == (191, 191, 191): #If end of round
            round_is_going = False
            print("End of round")
            wait_until_can_click_start_next_day()
            click_upgrades()
            buy_upgrades()
            click_back()
            wait_until_can_click_start_next_day()
            click_start_next_day()
            wait_until_round_starts()
            if pyautogui.pixel(1715, 52) == (255, 255, 255):
                print("Detected that we're moving on to new stage")
                press_next()
                time.sleep(5)
                break
            print("Starting next round")
            # Reset variables for new orund
            table_tracker = [True, True, True, True, True]  # True means table is available
            table_ordered_tracker = [False, False, False, False, False]
            order_queue = deque([])
            current_balance_image = pyautogui.screenshot('zero_dollars.png', region=(1613, 941, 117, 37))
            round_is_going = True


def play_stage_2():
    table_tracker = [True, True, True, True, True]  # True means table is available
    table_ordered_tracker = [False, False, False, False, False]
    order_queue = deque([])
    round_is_going = True
    current_balance_image = pyautogui.screenshot('zero_dollars.png', region=(1613, 941, 117, 37))

    while round_is_going and not keyboard.is_pressed('q'):
        penguins_are_waiting = check_if_penguin_waiting()
        if penguins_are_waiting and any(table_tracker):
            table_tracker = seat_waiting_penguin(table_tracker)
        order_queue = check_if_food_plate_ready(order_queue)
        table_ordered_tracker, order_queue = check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue, table_tracker)

        table_tracker, table_ordered_tracker, current_balance = check_if_money_on_any_tables(table_tracker,
                                                                                             table_ordered_tracker,
                                                                                             current_balance_image)

        if pyautogui.pixel(1732, 515) == (191, 191, 191):  # If end of round
            round_is_going = False
            print("End of round")
            wait_until_can_click_start_next_day()
            click_upgrades()
            buy_upgrades()
            click_back()
            click_start_next_day()
            wait_until_round_starts()
            if pyautogui.pixel(1715, 52) == (255, 255, 255):
                print("Detected that we're moving on to new stage")
                press_next()
                time.sleep(5)
                break
            print("Starting next round")
            # Reset variables for new orund
            table_tracker = [True, True, True, True, True]  # True means table is available
            table_ordered_tracker = [False, False, False, False, False]
            order_queue = deque([])
            current_balance_image = pyautogui.screenshot('zero_dollars.png', region=(1613, 941, 117, 37))
            round_is_going = True


def play_stage_3():
    table_tracker = [True, True, True, True, True]  # True means table is available
    table_ordered_tracker = [False, False, False, False, False]
    order_queue = deque([])
    round_is_going = True
    current_balance_image = pyautogui.screenshot('zero_dollars.png', region=(1613, 941, 117, 37))

    while round_is_going and not keyboard.is_pressed('q'):
        penguins_are_waiting = check_if_penguin_waiting()
        if penguins_are_waiting and any(table_tracker):
            table_tracker = seat_waiting_penguin(table_tracker)
        order_queue = check_if_food_plate_ready(order_queue)
        table_ordered_tracker, order_queue = check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue,
                                                                                table_tracker)

        table_tracker, table_ordered_tracker, current_balance = check_if_money_on_any_tables(table_tracker,
                                                                                             table_ordered_tracker,
                                                                                             current_balance_image)

        if pyautogui.pixel(1732, 515) == (191, 191, 191):  # If end of round
            round_is_going = False
            print("End of round")
            wait_until_can_click_start_next_day()
            click_upgrades()
            buy_upgrades()
            click_back()
            click_start_next_day()
            wait_until_round_starts()
            if pyautogui.pixel(1715, 52) == (255, 255, 255):
                print("Detected that we're moving on to new stage")
                press_next()
                time.sleep(5)
                break
            print("Starting next round")
            # Reset variables for new round
            table_tracker = [True, True, True, True, True]  # True means table is available
            table_ordered_tracker = [False, False, False, False, False]
            order_queue = deque([])
            current_balance_image = pyautogui.screenshot('zero_dollars.png', region=(1613, 941, 117, 37))
            round_is_going = True

def start_game():
    press_play()
    if pyautogui.pixel(849,442)[0] == 227:
        press_yes()
        time.sleep(2)
    else:
        press_next()
        time.sleep(.3)
        press_skip()
        time.sleep(.3)
        press_next()
        time.sleep(2)

def press_play():
    win32api.SetCursorPos((1639, 542))
    leftClick()
    time.sleep(.3)

def press_next():
    win32api.SetCursorPos((1625, 1009))
    leftClick()

def press_skip():
    win32api.SetCursorPos((950, 1014))
    leftClick()

def resume_previous_game():
    pass

def press_yes():
    win32api.SetCursorPos((849,442))
    leftClick()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.09)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click_table(table_number):
    if table_number == 1:
        win32api.SetCursorPos((728,313))
    elif table_number == 2:
        win32api.SetCursorPos((1375,318))
    elif table_number == 3:
        win32api.SetCursorPos((1053,529))
    elif table_number == 4:
        win32api.SetCursorPos((640, 787))
    else:
        win32api.SetCursorPos((1372,798))

    leftClick()


def click_penguin():
    win32api.SetCursorPos((480, 475))
    time.sleep(.1)
    leftClick()

def check_if_penguin_waiting():
    #  if background color, last or checks for purple tie on penguin
    if pyautogui.pixel(480, 475) == (197, 226, 228) or pyautogui.pixel(480, 475) == (233, 243, 245) or pyautogui.pixel(480, 475) == (234, 243, 246) or pyautogui.pixel(480, 475) == (200, 227, 234) or pyautogui.pixel(480, 475) == (201, 121, 177):
        return False
    else:
        return True


def seat_waiting_penguin(table_tracker):
    time.sleep(.05)
    click_penguin()

    if table_tracker[3] is True:
        click_table(4)
#        wait_until_penguin_sits(4)
        table_tracker[3] = False
    elif table_tracker[4] is True:
        click_table(5)
        #      wait_until_penguin_sits(5)
        table_tracker[4] = False
    elif table_tracker[2] is True:
        click_table(3)
        #       wait_until_penguin_sits(3)
        table_tracker[2] = False
    elif table_tracker[0] is True:
        click_table(1)
        #       wait_until_penguin_sits(1)
        table_tracker[0] = False
    elif table_tracker[1] is True:
        click_table(2)
        #     wait_until_penguin_sits(2)
        table_tracker[1] = False

    print("Updated Table Tracker: ", table_tracker)
    return table_tracker


def check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue, table_tracker):
    if not table_ordered_tracker[0] and pyautogui.pixel(923, 250) == (129, 129, 129) and table_tracker[0] == False:
        print("clicking table 1 because table is ready to order")
        click_table(1)
        wait_until_order_taken(1)
        table_ordered_tracker[0] = True
        print("Updated table_ordered_tracker:", table_ordered_tracker)
        # if a 2nd person is at this table
        if pyautogui.pixel(561, 396) == (255, 191, 43):
            print("2 people at table 1")
            order_queue.append(1)
        order_queue.append(1)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[1] and pyautogui.pixel(1571, 250) == (129, 129, 129) and not pyautogui.pixel(1571, 250) == (255,255,255) and table_tracker[1] == False:
        print("clicking table 2 because table is ready to order")
        click_table(2)
        wait_until_order_taken(2)
        table_ordered_tracker[1] = True
        print("Updated table_ordered_tracker:", table_ordered_tracker)
        if pyautogui.pixel(1208, 392) == (255, 191, 43):
            print("2 people at table 2")
            order_queue.append(2)
        order_queue.append(2)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[2] and pyautogui.pixel(1248, 466) == (128, 128, 128) and table_tracker[2] == False:
        print("clicking table 3 because table is ready to order")
        click_table(3)
        wait_until_order_taken(3)
        table_ordered_tracker[2] = True
        print("Updated table_ordered_tracker:", table_ordered_tracker)
        if pyautogui.pixel(888,604) == (255, 191, 43):
            print("2 people at table 3")
            order_queue.append(3)
        order_queue.append(3)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if (not table_ordered_tracker[3]) and pyautogui.pixel(926, 740) == (123, 123, 123) and table_tracker[3] == False:
        print("clicking table 4 because table is ready to order")
        click_table(4)
        wait_until_order_taken(4)
        table_ordered_tracker[3] = True
        print("Updated table_ordered_tracker:", table_ordered_tracker)
        if pyautogui.pixel(564, 877) == (255, 191, 43):
            print("2 people at table 4")
            order_queue.append(4)
        order_queue.append(4)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[4] and pyautogui.pixel(1572, 737) == (127, 127, 127) and table_tracker[4] == False:
        print("clicking table 5 because table is ready to order")
        click_table(5)
        wait_until_order_taken(5)
        table_ordered_tracker[4] = True
        print("Updated table_ordered_tracker:", table_ordered_tracker)
        if pyautogui.pixel(1212, 877) == (255, 191, 43):
            print("2 people at table 5")
            order_queue.append(5)
        order_queue.append(5)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    else:
        return table_ordered_tracker, order_queue


def check_if_food_plate_ready(order_queue):
    #  check if game over before doing anything here, sometimes game would crash here when round is over
    if pyautogui.pixel(1732, 515) == (191, 191, 191):
        return

    # if need to get 2 plates at once because 2 penguins are at 1 table
    if len(order_queue) > 1 and order_queue[0] == order_queue[1]:
        # If plate 1 exists and is not gray?
        if pyautogui.pixel(929, 1023)[0] != 255 and pyautogui.pixel(769, 1042)[0] != 255 and not pyautogui.pixel(929, 1023) == (140, 140, 140):
            print("Going to take 2 plates at once")
            click_plate(1)
            time.sleep(.15)
            click_plate(2)
            wait_until_plate_picked_up(2)
            print("clicking table", order_queue[0], " because I have both their foods in my hand")
            current_table = order_queue[0]
            click_table(order_queue.popleft())
            wait_until_food_at_table(current_table)
            order_queue.popleft()
            print("Updated order_queue: ", order_queue)
            return order_queue
        # else if plate 2 exists
        elif pyautogui.pixel(769, 1042)[0] != 255 and pyautogui.pixel(612, 1046)[0] != 255 and not pyautogui.pixel(769, 1042) == (140, 140, 140):
            print("Going to take 2 plates at once")
            click_plate(2)
            time.sleep(.02)
            click_plate(3)
            wait_until_plate_picked_up(3)
            print("clicking table", order_queue[0], " because I have both their foods in my hand")
            current_table = order_queue[0]
            click_table(order_queue.popleft())
            wait_until_food_at_table(current_table)
            order_queue.popleft()
            print("Updated order_queue: ", order_queue)
            return order_queue
        # else if plate 3 exists
        elif pyautogui.pixel(612, 1046)[0] != 255 and not pyautogui.pixel(612, 1046) == (140, 140, 140):
            print("Going to take 2 plates at once, plate 3 and 4")
            click_plate(3)
            time.sleep(.09)
            click_plate(4)
            wait_until_plate_picked_up(4)
            print("clicking table", order_queue[0], " because I have both their foods in my hand")
            current_table = order_queue[0]
            click_table(order_queue.popleft())
            wait_until_food_at_table(current_table)
            order_queue.popleft()
            print("Updated order_queue: ", order_queue)
            return order_queue
        else:
            return order_queue
    # if plate 1 is ready
    elif pyautogui.pixel(929, 1023)[0] != 255:
        click_plate(1)
        wait_until_plate_picked_up(1)
        print("clicking table",order_queue[0]," because I have their food in my hand")
        current_table = order_queue[0]
        click_table(order_queue.popleft())
        wait_until_food_at_table(current_table)
        print("Updated order_queue: ", order_queue)
        return order_queue
    # if plate 2 is ready
    elif pyautogui.pixel(769, 1042)[0] != 255:
        click_plate(2)
        wait_until_plate_picked_up(2)
        print("clicking table",order_queue[0]," because I have their food in my hand")
        current_table = order_queue[0]
        click_table(order_queue.popleft())
        wait_until_food_at_table(current_table)
        print("Updated order_queue: ", order_queue)
        return order_queue
    # if plate 3 is ready
    elif pyautogui.pixel(612, 1046)[0] != 255:
        click_plate(3)
        wait_until_plate_picked_up(3)
        print("clicking table", order_queue[0], " because I have their food in my hand")
        current_table = order_queue[0]
        click_table(order_queue.popleft())
        wait_until_food_at_table(current_table)
        print("Updated order_queue: ", order_queue)
        return order_queue
    # if plate 4 is ready
    elif pyautogui.pixel(448, 1046)[0] != 255:
        click_plate(4)
        wait_until_plate_picked_up(4)
        print("clicking table", order_queue[0], " because I have their food in my hand")
        current_table = order_queue[0]
        click_table(order_queue.popleft())
        wait_until_food_at_table(current_table)
        print("Updated order_queue: ", order_queue)
        return order_queue
    # if plate 5 is ready
    elif pyautogui.pixel(286, 1046)[0] != 255:
        click_plate(5)
        wait_until_plate_picked_up(5)
        print("clicking table", order_queue[0], " because I have their food in my hand")
        current_table = order_queue[0]
        click_table(order_queue.popleft())
        wait_until_food_at_table(current_table)
        print("Updated order_queue: ", order_queue)
        return order_queue
    return order_queue

def click_plate(plate_number):
    if plate_number == 1:
        win32api.SetCursorPos((929, 1023))
        time.sleep(0.1)
        leftClick()

    elif plate_number == 2:
        win32api.SetCursorPos((769, 1023))
        time.sleep(0.02)
        leftClick()

    elif plate_number == 3:
        win32api.SetCursorPos((613, 1023))
        time.sleep(0.02)
        leftClick()

    elif plate_number == 4:
        win32api.SetCursorPos((443, 1023))
        time.sleep(0.02)
        leftClick()

    elif plate_number == 5:
        win32api.SetCursorPos((283, 1023))
        time.sleep(0.02)
        leftClick()


def check_if_money_on_any_tables(table_tracker, table_ordered_tracker, current_balance_image):
    # if can see the gold money or (if seat is empty and order was taken)
    if (pyautogui.pixel(912, 356) == (197,226,228) or pyautogui.pixel(912, 356) == (200, 227, 234)) and table_ordered_tracker[0] == True:
        print("clicking table 1 because there is money on the table")
        click_table(1)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[0] = True
        table_ordered_tracker[0] = False

    if (pyautogui.pixel(1559, 356) == (197, 226, 228) or pyautogui.pixel(1559, 356) == (200, 227, 234)) and table_ordered_tracker[1] == True:
        print("clicking table 2 because there is money on the table")
        click_table(2)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[1] = True
        table_ordered_tracker[1] = False

    if (pyautogui.pixel(1238, 586) == (197, 226, 228) or pyautogui.pixel(1238, 586) == (200, 227, 234)) and table_ordered_tracker[2] == True:
        print("clicking table 3 because there is money on the table")
        click_table(3)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[2] = True
        table_ordered_tracker[2] = False

    if (pyautogui.pixel(914, 844) == (197, 226, 228) or pyautogui.pixel(914, 844) == (200, 227, 234)) and table_ordered_tracker[3] == True:
        print("clicking table 4 because there is money on the table")
        click_table(4)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[3] = True
        table_ordered_tracker[3] = False
    if (pyautogui.pixel(1551, 844) == (197, 226, 228) or pyautogui.pixel(1551, 844) == (200, 227, 234)) and table_ordered_tracker[4] == True:
        print("clicking table 5 because there is money on the table")
        click_table(5)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[4] = True
        table_ordered_tracker[4] = False
    return table_tracker, table_ordered_tracker, current_balance_image

def wait_until_penguin_sits(table_number):
    if table_number == 1:
        while pyautogui.pixel(915,347) == (197, 226, 228) or pyautogui.pixel(915,347) == (200, 227, 234):
            pass
    elif table_number == 2:
        while pyautogui.pixel(1558,361) == (197, 226, 228) or pyautogui.pixel(1558,361) == (200, 227, 234):
            pass
    elif table_number == 3:
        while pyautogui.pixel(1236,556) == (197, 226, 228) or pyautogui.pixel(1236,556) == (200, 227, 234):
            pass
    elif table_number == 4:
        while pyautogui.pixel(914,840) == (197, 226, 228) or pyautogui.pixel(914,840) == (200, 227, 234):
            pass
    elif table_number == 5:
        while pyautogui.pixel(1555,828) == (197, 226, 228) or pyautogui.pixel(1555,828) == (200, 227, 234):
            pass


def wait_until_plate_picked_up(plate_number):
    return
    # if plate_number == 1:
    #     while not pyautogui.pixel(930, 1030) == (255, 255, 255):
    #         pass
    #
    # elif plate_number == 2:
    #     while not pyautogui.pixel(768, 1030) == (255, 255, 255):
    #         pass
    #
    # elif plate_number == 3:
    #     while not pyautogui.pixel(606, 1030) == (255, 255, 255):
    #         pass
    #
    # elif plate_number == 4:
    #     while not pyautogui.pixel(444, 1030) == (255, 255, 255):
    #         pass
    #
    # elif plate_number == 5:
    #     while not pyautogui.pixel(282, 1030) == (255, 255, 255):
    #         pass

def wait_until_food_at_table(table_number):
   # or statement in tables 1 and 2 because the stage background might affect it
    if table_number == 1:
        while pyautogui.pixel(838, 229) == (16, 18, 15) or pyautogui.pixel(838, 229) == (13, 16, 14) or pyautogui.pixel(838, 229) == (14, 16, 14):
            pass
    elif table_number == 2:
        while pyautogui.pixel(1485, 229) == (15, 16, 14) or pyautogui.pixel(1485, 229) == (12, 14, 12) or pyautogui.pixel(1485, 229) == (7, 10, 11) or pyautogui.pixel(1485, 229) ==(8, 11, 12):
            pass
    elif table_number == 3:
        while pyautogui.pixel(1143, 433) == (255, 255, 255):
            pass
    elif table_number == 4:
        while pyautogui.pixel(818, 698) == (255, 255, 255):
            pass
    elif table_number == 5:
        while pyautogui.pixel(1469, 703) == (255, 255, 255):
            pass
    print("Food got to table.")


def wait_until_order_taken(table_number):
    if table_number == 1:
        while pyautogui.pixel(836, 229)[0] > 125: #If RGB is low, then order was taken
            pass
    elif table_number == 2:
        while pyautogui.pixel(1485, 228)[0] > 125:
            pass
    elif table_number == 3:
        while pyautogui.pixel(1143, 433) != (255, 255, 255):
            pass
    elif table_number == 4:
        while pyautogui.pixel(818, 698) != (255, 255, 255):
            pass
    elif table_number == 5:
        while pyautogui.pixel(1469, 703) != (255, 255, 255):
            pass

def wait_until_money_collected(current_balance_image):
    current_balance_image = check_if_balance_changed(current_balance_image)
    return current_balance_image


def click_start_next_day():
    win32api.SetCursorPos((724, 778))
    leftClick()
    time.sleep(.3)


def check_if_balance_changed(current_balance_image):
    balance_changed = False
    while balance_changed == False:
        if pyautogui.locateOnScreen(current_balance_image, region=(1613, 941, 117, 37), confidence=.9):
            pass
        else:
            new_balance_image = pyautogui.screenshot(region=(1613, 941, 117, 37))
            return new_balance_image


def wait_until_can_click_start_next_day():
    while True:
        if pyautogui.pixel(740, 778) == (221, 42, 36):
            return
        pass


def click_upgrades():
    win32api.SetCursorPos((1111, 777))
    leftClick()
    time.sleep(.3)


def buy_upgrades():
    #Buy all upgrades starting with left bottom, going up, then starting middle bottom, repeat
    win32api.SetCursorPos((714, 774))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((714, 505))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((714, 246))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((1111, 774))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((1111, 505))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((1111, 246))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((1518, 774))
    leftClick()
    time.sleep(.05)

    win32api.SetCursorPos((1518, 505))
    leftClick()
    time.sleep(.1)

    win32api.SetCursorPos((1518, 246))
    leftClick()
    time.sleep(.05)

def click_back():
    win32api.SetCursorPos((1631, 1015))
    time.sleep(.05)
    leftClick()
    time.sleep(.5)


def wait_until_round_starts():
    while True:
        if pyautogui.pixel(159, 656) == (255, 204, 7) or pyautogui.pixel(159, 656) == (255, 204, 8):
            time.sleep(1)
            return
        else:
            pass

main()
