import decimal
import sys
from collections import deque
from queue import Queue
import pyautogui
import time
import pytesseract
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
    if pyautogui.pixel(186, 73)[0] == 151:
        print("in middle of round on stage 1")
        play_stage_1()
        play_stage_2()
        #play_stage_3()

    elif pyautogui.pixel(1342, 69) == (255, 155, 8):
        print("We are in middle of round on stage 2")
        play_stage_2()
        #play_stage_3()
    else:
        print("We are at start screen")
        start_game()
        play_stage_1()
        play_stage_2()
        #play_stage_3()


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
        table_ordered_tracker, order_queue = check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue)
        order_queue = check_if_food_plate_ready(order_queue)
        table_tracker, table_ordered_tracker, current_balance = check_if_money_on_any_tables(table_tracker, table_ordered_tracker, current_balance_image)

        if pyautogui.pixel(1732, 515) == (191, 191, 191): #If end of round
            round_is_going = False
            print("End of round")
            wait_until_can_click_start_next_day()
            click_start_next_day()
            time.sleep(5)
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
        table_ordered_tracker, order_queue = check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue)
        order_queue = check_if_food_plate_ready(order_queue)
        table_tracker, table_ordered_tracker, current_balance = check_if_money_on_any_tables(table_tracker,
                                                                                             table_ordered_tracker,
                                                                                             current_balance_image)

        if pyautogui.pixel(1732, 515) == (191, 191, 191):  # If end of round
            round_is_going = False
            print("End of round")
            wait_until_can_click_start_next_day()
            click_start_next_day()
            time.sleep(5)
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

def start_game():
    press_play()
    if pyautogui.pixel(849,442)[0] == 227:
        press_yes()
        time.sleep(2)
    else:
        press_next()
        press_skip()
        press_next()
        time.sleep(2)

def press_play():
    win32api.SetCursorPos((1639, 542))
    leftClick()
    time.sleep(.3)

def press_next():
    win32api.SetCursorPos((1625, 1009))
    leftClick()
    time.sleep(.3)

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
    if pyautogui.pixel(480, 475) == (197, 226, 228):
        return False
    else:
        return True



def seat_waiting_penguin(table_tracker):
    time.sleep(.05)
    click_penguin()

    if table_tracker[3] is True:
        click_table(4)
        wait_until_penguin_sits(4)
        table_tracker[3] = False
    elif table_tracker[4] is True:
        click_table(5)
        wait_until_penguin_sits(5)
        table_tracker[4] = False
    elif table_tracker[2] is True:
        click_table(3)
        wait_until_penguin_sits(3)
        table_tracker[2] = False
    elif table_tracker[0] is True:
        click_table(1)
        wait_until_penguin_sits(1)
        table_tracker[0] = False
    elif table_tracker[1] is True:
        click_table(2)
        wait_until_penguin_sits(2)
        table_tracker[1] = False



    print("Updated Table Tracker: ", table_tracker)
    return table_tracker

def check_if_any_tables_ready_to_order(table_ordered_tracker, order_queue):
    if not table_ordered_tracker[0] and pyautogui.pixel(923, 250)[0] == pyautogui.pixel(923, 250)[1]:
        print("clicking table 1 because table is ready to order")
        click_table(1)
        wait_until_order_taken(1)
        table_ordered_tracker[0] = True
        # if a 2nd person is at this table
        if pyautogui.pixel(566, 377) != (197, 226, 228):
            print("2 people at table 1")
            order_queue.append(1)
        order_queue.append(1)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[1] and pyautogui.pixel(1571, 250)[0] == pyautogui.pixel(1571, 250)[1]:
        print("clicking table 2 because table is ready to order")
        click_table(2)
        wait_until_order_taken(2)
        table_ordered_tracker[1] = True
        if pyautogui.pixel(1182, 258) != (185, 216, 223):
            print("2 people at table 2")
            order_queue.append(2)
        order_queue.append(2)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[2] and pyautogui.pixel(1248, 466)[0] == pyautogui.pixel(1248, 466)[1]:
        print("clicking table 3 because table is ready to order")
        click_table(3)
        wait_until_order_taken(3)
        table_ordered_tracker[2] = True
        if pyautogui.pixel(859, 580) != (197, 226, 228):
            print("2 people at table 3")
            order_queue.append(3)
        order_queue.append(3)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[3] and pyautogui.pixel(926, 740)[0] == pyautogui.pixel(926, 740)[1]:
        print("clicking table 4 because table is ready to order")
        click_table(4)
        wait_until_order_taken(4)
        table_ordered_tracker[3] = True
        if pyautogui.pixel(541, 841) != (197, 226, 228):
            print("2 people at table 4")
            order_queue.append(4)
        order_queue.append(4)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    if not table_ordered_tracker[4] and pyautogui.pixel(1572, 737)[0] == pyautogui.pixel(1572, 737)[1]:
        print("clicking table 5 because table is ready to order")
        click_table(5)
        wait_until_order_taken(5)
        table_ordered_tracker[4] = True
        if pyautogui.pixel(1189, 850) != (197, 226, 228):
            print("2 people at table 5")
            order_queue.append(5)
        order_queue.append(5)
        print("Updated order_queue: ", order_queue)
        return table_ordered_tracker, order_queue

    else:
        return table_ordered_tracker, order_queue


def check_if_food_plate_ready(order_queue):
    # if need to get 2 plates at once because 2 penguins are at 1 table
    if len(order_queue) > 1 and order_queue[0] == order_queue[1]:
        print("Detected that I will need to get 2 plates")
        if pyautogui.pixel(929, 1023)[0] != 255 and not pyautogui.pixel(929, 1023) == (140, 140, 140):
            print("Going to take 2 plates at once")
            click_plate(1)
            wait_until_plate_picked_up(1)
            click_plate(2)
            wait_until_plate_picked_up(2)
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
    return order_queue

def click_plate(plate_number):
    if plate_number == 1:
        win32api.SetCursorPos((929, 1023))
        leftClick()

    if plate_number == 2:
        win32api.SetCursorPos((769, 1023))
        leftClick()


def check_if_money_on_any_tables(table_tracker, table_ordered_tracker, current_balance_image):
    # if can see the gold money or (if seat is empty and order was taken)
    if pyautogui.pixel(912, 356) == (197,226,228) and table_ordered_tracker[0] == True:
        print("clicking table 1 because there is money on the table")
        click_table(1)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[0] = True
        table_ordered_tracker[0] = False

    if pyautogui.pixel(1559, 356) == (197,226,228) and table_ordered_tracker[1] == True:
        print("clicking table 2 because there is money on the table")
        click_table(2)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[1] = True
        table_ordered_tracker[1] = False

    if pyautogui.pixel(1238, 586) == (197, 226, 228) and table_ordered_tracker[2] == True:
        print("clicking table 3 because there is money on the table")
        click_table(3)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[2] = True
        table_ordered_tracker[2] = False

    if pyautogui.pixel(914, 844) == (197, 226, 228) and table_ordered_tracker[3] == True:
        print("clicking table 4 because there is money on the table")
        click_table(4)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[3] = True
        table_ordered_tracker[3] = False
    if pyautogui.pixel(1551, 844) == (197, 226, 228) and table_ordered_tracker[4] == True:
        print("clicking table 5 because there is money on the table")
        click_table(5)
        current_balance_image = wait_until_money_collected(current_balance_image)
        table_tracker[4] = True
        table_ordered_tracker[4] = False
    return table_tracker, table_ordered_tracker, current_balance_image

def wait_until_penguin_sits(table_number):
    if table_number == 1:
        while pyautogui.pixel(915,347) == (197, 226, 228):
            pass
    elif table_number == 2:
        while pyautogui.pixel(1558,361) == (197, 226, 228):
            pass
    elif table_number == 3:
        while pyautogui.pixel(1236,556) == (197, 226, 228):
            pass
    elif table_number == 4:
        while pyautogui.pixel(914,840) == (197, 226, 228):
            pass
    elif table_number == 5:
        while pyautogui.pixel(1555,828) == (197, 226, 228):
            pass


def wait_until_plate_picked_up(plate_number):
    if plate_number == 1:
        while not pyautogui.pixel(930, 1030) == (255,255,255):
            pass

    if plate_number == 2:
        while not pyautogui.pixel(768, 1030) == (255, 255, 255):
            pass

def wait_until_food_at_table(table_number):
    if table_number == 1:
        while not pyautogui.pixel(820, 211) == (255, 255, 255):
            pass
    elif table_number == 2:
        while not pyautogui.pixel(1467, 212) == (255, 255, 255):
            pass
    elif table_number == 3:
        while not pyautogui.pixel(1143, 433) == (255, 255, 255):
            pass
    elif table_number == 4:
        while pyautogui.pixel(818, 698) == (255, 255, 255):
            pass
    elif table_number == 5:
        while pyautogui.pixel(1469, 703) == (255, 255, 255):
            pass

def wait_until_order_taken(table_number):
    if table_number == 1:
        while pyautogui.pixel(820, 211) == (185, 216, 223):
            pass
    elif table_number == 2:
        while pyautogui.pixel(1467, 212) == (185, 216, 223):
            pass
    elif table_number == 3:
        while not pyautogui.pixel(1143, 433) == (117, 146, 162):
            pass
    elif table_number == 4:
        while pyautogui.pixel(818, 698) == (197, 226, 228):
            pass
    elif table_number == 5:
        while pyautogui.pixel(1469, 703) == (197, 226, 228):
            pass


def click_start_next_day():
    win32api.SetCursorPos((724, 778))
    leftClick()
    time.sleep(.3)

def wait_until_money_collected(current_balance_image):
    current_balance_image = check_if_balance_changed(current_balance_image)
    return current_balance_image


def check_if_balance_changed(current_balance_image):
    balance_changed = False
    while balance_changed == False:
        if pyautogui.locateOnScreen(current_balance_image, region=(1613, 941, 117, 37), confidence=.8):
            pass
        else:
            new_balance_image = pyautogui.screenshot(region=(1613, 941, 117, 37))
            return new_balance_image

def wait_until_can_click_start_next_day():
    time.sleep(4)

def check_current_stage():


    if pyautogui.pixel(1340, 70) == (255, 154, 25):
        current_stage = 2

    return current_stage

main()
