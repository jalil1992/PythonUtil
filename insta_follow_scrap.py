        if self.follower_limit != 0:
        label5.pack(side='left', expand=True, fill='both')
from tkinter import filedialog
import openpyxl
import xlrd
from tkinter import messagebox
import threading
import os
import time
class MainView:
api = None


def login(username, password):
        logout()
    api = InstagramAPI(username, password)



def logout():
    global api
    if api.isLoggedIn:
        api.logout()
                    self.target_user['status'] = 'not found'

class StoppableThread(threading.Thread):
    def __init__(self, target):
        super(StoppableThread, self).__init__(target=target)
            source_sheet.cell(row=2, column=3).value = self.follower_limit
        # self.is_stopped = False

    def stop(self):
        self.users = []
        # self.is_stopped = True

    def stopped(self):
        return self._stop_event.is_set()

                                    home_following_sheet.cell(row=ind, column=3).value = api.LastJson['user']['following_count']
class MainView:
    def __init__(self, master):
        self.master = master
import tkinter as tk

        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(3, weight=1)

        frame1 = tk.Frame(master, pady=3)

        frame3 = tk.Frame(master, pady=3)
        frame4 = tk.Frame(master, pady=3)
        frame5 = tk.Frame(master, pady=3)

                                                print('sleeping for a minute')
        frame2.grid(row=1, sticky='ew')
        frame3.grid(row=2, sticky='ew')
                user['total_count'] = follower_count
        frame5.grid(row=4, sticky='ew')
                    self.update_progress()
        tk.Label(frame1, text='Select excel file : ', width=15, anchor='e').pack(side='left')
        self.excel_file = tk.StringVar()
        tk.Entry(frame1, width=50, textvariable=self.excel_file).pack(side='left', expand=True)
    root.mainloop()
        tk.Label(frame2, text='Username : ', width=15, anchor='e').pack(side='left')
                if api.LastJson['message'] == 'Please wait a few minutes before you try again.':
            while self.thread.isAlive():

        tk.Label(frame3, text='Password : ', width=15, anchor='e').pack(side='left')
                        time.sleep(60)
        tk.Entry(frame3, width=50, textvariable=self.password).pack(side='left', expand=True)

        browse1_button = tk.Button(frame1, text="Browse", width=8, command=self.browse_excel_file)
        browse1_button.pack(side='right')

                                        break
        label5 = tk.Label(frame4, textvariable=self.progress, borderwidth=2, relief='groove')
        label5.pack(side='left', expand=True, fill='both')

        self.button_text = tk.StringVar()
        self.button_text.set("Start")
        toggle_button = tk.Button(frame5, textvariable=self.button_text, width=8, command=self.toggle)
        toggle_button.pack()

        frame5 = tk.Frame(master, pady=3)
        self.users = []
        self.target_user = {}
                    break

    def browse_excel_file(self):
        text = filedialog.askopenfilename(title='Select input excel file', filetypes=[("Excel files", "*.xlsx")])
                                    home_following_sheet.cell(row=ind, column=1).value = following_name
            self.excel_file.set(text)

    def toggle(self):

            if self.excel_file.get() == '':
                messagebox.showerror('Error', 'Please input proper paths')
                                    ind += 1
            if len(str(source_sheet.row(1)[2].value)) != 0:
import tkinter as tk
import openpyxl
                following_count = api.LastJson['user']['following_count']
            while self.thread.isAlive():
            self.follower_limit = 0
        self.target_user = {}
import threading
                                    else:
            xls = xlrd.open_workbook(self.excel_file.get())
        self.progress = tk.StringVar()
            self.excel_file.set(text)


                self.users.append({'name': str(source_sheet.row(row)[0].value),
                                   'status': 'pending'})
        self.follower_limit = 0

                                    else:
                self.target_user['name'] = str(source_sheet.row(1)[1].value)
            if len(str(source_sheet.row(1)[2].value)) != 0:
                self.follower_limit = int(source_sheet.row(1)[2].value)

            if not login(self.username.get(), self.password.get()):
                                    ind += 1
                return
            self.thread = StoppableThread(self.scrap_data)
            self.thread.setDaemon(True)
            elif user['status'] == 'not found':
                                                break
        else:
                        if 'next_max_id' in api.LastJson:
            self.thread = StoppableThread(self.scrap_data)

            self.thread = None
                    self.target_user['status'] = 'not found'
            logout()
        pass

    def update_progress(self):
        message = ''
            self.button_text.set("Stop")
            if user['status'] == 'pending':

        frame3 = tk.Frame(master, pady=3)
                message += '-->working on %s followers(%d/%d)\n' % (user['name'], user['worked_count'], user['total_count'])
            while self.thread.isAlive():
                                        all_followers[follower_name]['cnt'] += 1
            elif user['status'] == 'error':
                message += 'error occurred on %s\n' % user['name']
            elif user['status'] == 'not found':
                                while not api.searchUsername(following_name) or 'user' not in api.LastJson:
            elif user['status'] == 'completed':
                message += 'completed scraping on %s\n' % user['name']
                                self.update_progress()

    def scrap_data(self):
        output_file = self.excel_file.get().replace('.xls', '_result.xls')
        book = openpyxl.Workbook()
        source_sheet = book.active
                        if len(api.LastJson['users']) == 0:
        follower_sheet = book.create_sheet('results')
        summary_sheet = book.create_sheet('summary')
        home_follower_sheet = book.create_sheet('home followers')
                        else:
        home_follow_delta_sheet = book.create_sheet('home follow delta')
                        if api.LastJson['status'] != 'ok':
                self.target_user['status'] = 'working following'

        source_sheet.cell(row=1, column=1).value = 'target account'

                                    if api.LastJson['message'] == 'Please wait a few minutes before you try again.':

        ind = 2
        self.follower_limit = 0
            source_sheet.cell(row=ind, column=1).value = user['name']
                messagebox.showerror('Error', 'Login failed')
        follower_sheet.cell(row=1, column=1).value = 'target account'
        follower_sheet.cell(row=1, column=2).value = 'username'
        source_sheet = book.active
        follower_sheet.cell(row=1, column=4).value = 'followings'
        summary_sheet.cell(row=1, column=1).value = 'unique users from results'
        summary_sheet.cell(row=1, column=2).value = 'target following'
        summary_sheet.cell(row=1, column=3).value = 'follower count'
        summary_sheet.cell(row=1, column=4).value = 'following count'
        home_follower_sheet.cell(row=1, column=1).value = 'username'
        home_follower_sheet.cell(row=1, column=2).value = 'follower count'
        home_follower_sheet.cell(row=1, column=3).value = 'following count'
        home_following_sheet.cell(row=1, column=1).value = 'username'

        home_following_sheet.cell(row=1, column=3).value = 'following count'
                            max_id = api.LastJson['next_max_id']
            temp = [follower_name, value['cnt'], value['follower_cnt'], value['following_cnt']]
        if self.follower_limit != 0:
            source_sheet.cell(row=2, column=3).value = self.follower_limit
                                    home_follower_sheet.cell(row=ind, column=3).value = api.LastJson['user']['following_count']
        if len(self.target_user['name']) > 0:
            source_sheet.cell(row=2, column=2).value = self.target_user['name']
            while not api.searchUsername(self.target_user['name']) or 'user' not in api.LastJson:

                    print('sleeping for a minute')

                else:
                    self.target_user['status'] = 'not found'
        for follower_name, value in all_followers.items():
                    print('sleeping for a minute')

            ind = 2
                        time.sleep(60)
                user_id = api.LastJson['user']['pk']
                follower_count = api.LastJson['user']['follower_count']
                following_count = api.LastJson['user']['following_count']
                max_id = ''


                self.target_user['total_count'] = follower_count
                self.target_user['worked_count'] = 0
        ind = 2

                while True:
                        if api.LastJson['status'] != 'ok':

                else:
                        api.getUserFollowers(str(user_id), max_id)
                        has_max_id = False
                        if api.LastJson['status'] != 'ok':
    def __init__(self, master):
                            time.sleep(60)
                                        follower_sheet.cell(row=ind, column=2).value = follower_name

        book = openpyxl.Workbook()
                            max_id = api.LastJson['next_max_id']
                            has_max_id = True

        source_sheet.cell(row=1, column=3).value = 'exclude users with follower count less than'
                            break
                        else:
                        else:
                                follower_name = follower['username']
        summary_sheet.cell(row=1, column=4).value = 'following count'

                                while not api.searchUsername(follower_name) or 'user' not in api.LastJson:
                                    if api.LastJson['message'] == 'Please wait a few minutes before you try again.':
                                        print('sleeping for a minute')
                                        time.sleep(60)
                    try:
                                        break

                                if 'user' in api.LastJson:
                                    home_follower_sheet.cell(row=ind, column=1).value = follower_name
                                    home_follower_sheet.cell(row=ind, column=2).value = api.LastJson['user']['follower_count']
        frame5.grid(row=4, sticky='ew')
                                    ind += 1

                                self.target_user['worked_count'] += 1
                                self.update_progress()

                        if not has_max_id:
                            break

                        print(ex)
        frame3 = tk.Frame(master, pady=3)
                        time.sleep(60)

                self.target_user['status'] = 'working following'
                self.target_user['total_count'] = following_count
            source_sheet.cell(row=2, column=2).value = self.target_user['name']
                            break
                                while not api.searchUsername(following_name) or 'user' not in api.LastJson:
        book.save(output_file)
        self._stop_event = threading.Event()
import threading

                while True:
                                follower_name = follower['username']
                        return
                    try:
                        api.getUserFollowings(str(user_id), max_id)
                return
                                                print('sleeping for a minute')
                                        all_followers[follower_name]['cnt'] += 1

            if len(str(source_sheet.row(1)[2].value)) != 0:

                        if 'next_max_id' in api.LastJson:
                            max_id = api.LastJson['next_max_id']
                            has_max_id = True

                        if len(api.LastJson['users']) == 0:
        pass
                        else:
                            for following in api.LastJson['users']:
                                following_name = following['username']

                                while not api.searchUsername(following_name) or 'user' not in api.LastJson:
                                    if api.LastJson['message'] == 'Please wait a few minutes before you try again.':
                                    home_following_sheet.cell(row=ind, column=1).value = following_name
                    try:
                                    else:
                                        break
                        has_max_id = False
                                if 'user' in api.LastJson:
                                    home_following_sheet.cell(row=ind, column=1).value = following_name
                                    home_following_sheet.cell(row=ind, column=2).value = api.LastJson['user']['follower_count']
                                    home_following_sheet.cell(row=ind, column=3).value = api.LastJson['user']['following_count']
                                    ind += 1

                    break
                        print(ex)
                                    delta_ind += 1

                                self.target_user['worked_count'] += 1
            source_sheet.cell(row=ind, column=1).value = user['name']

                        if not has_max_id:
                follower_count = api.LastJson['user']['follower_count']
                    except Exception as ex:
                        print(ex)
                        print('sleeping for a minute')
        toggle_button.pack()

            if 'working' in self.target_user['status']:
                self.target_user['status'] = 'completed'
                self.update_progress()
        self.button_text = tk.StringVar()
        ind = 2
        label5.pack(side='left', expand=True, fill='both')
            if self.thread.stopped():
                return

            if self.excel_file.get() == '':
                if api.LastJson['message'] == 'Please wait a few minutes before you try again.':
                message += 'error occurred on %s\n' % user['name']
                    time.sleep(60)
                self.update_progress()


    global api
                self.follower_limit = int(source_sheet.row(1)[2].value)
            if api.LastJson['status'] == 'ok':

        self.users = []
                max_id = ''
            self.button_text.set("Stop")
                user['status'] = 'working follower'
                user['total_count'] = follower_count

from tkinter import filedialog

                    if self.thread.stopped():
                        return
            self.thread = StoppableThread(self.scrap_data)
                        api.getUserFollowers(str(user_id), max_id)
                                        print('sleeping for a minute')
                        if api.LastJson['status'] != 'ok':
                            print('sleeping for a minute')

                            continue

        tk.Label(frame2, text='Username : ', width=15, anchor='e').pack(side='left')
        all_followers_list = sorted(all_followers_list, key=lambda x: (-x[1], -x[2]))
                            has_max_id = True
            ind = 2
                        if len(api.LastJson['users']) == 0:
                            break
                        else:
                            for follower in api.LastJson['users']:
                    break
        source_sheet.cell(row=1, column=3).value = 'exclude users with follower count less than'
                                if follower_name not in home_followers:
                                    if follower_name not in all_followers:
                                        while not api.searchUsername(follower_name) or 'user' not in api.LastJson:
                                            if api.LastJson['message'] == 'Please wait a few minutes before you try again.':
                                                print('sleeping for a minute')
                        if not has_max_id:
                                            else:
            ind = 2
        source_sheet.cell(row=1, column=2).value = 'exclude followers from'

                                            all_followers[follower_name] = {}
                                            all_followers[follower_name]['cnt'] = 1
                        time.sleep(60)
                messagebox.showerror('Error', 'Login failed')
                                            follower_sheet.cell(row=ind, column=1).value = user['name']
                                            follower_sheet.cell(row=ind, column=2).value = follower_name
            if len(str(source_sheet.row(1)[2].value)) != 0:
        label5.pack(side='left', expand=True, fill='both')
                                if 'user' in api.LastJson:
                                    else:
                                        all_followers[follower_name]['cnt'] += 1
        frame3.grid(row=2, sticky='ew')
                                        follower_sheet.cell(row=ind, column=2).value = follower_name
                                        follower_sheet.cell(row=ind, column=2).value = follower_name
                                follower_name = follower['username']
                                        ind += 1

                                self.update_progress()

                        if not has_max_id:
                            break
                    except Exception as ex:
                        print(ex)
                        print('sleeping for a minute')
                        time.sleep(60)

                self.thread.join(1)
                user['status'] = 'completed'
                                self.update_progress()
                messagebox.showerror('Error', 'Please input proper paths')
        all_followers_list = []
                if api.LastJson['message'] == 'Please wait a few minutes before you try again.':
            temp = [follower_name, value['cnt'], value['follower_cnt'], value['following_cnt']]

        home_follower_sheet = book.create_sheet('home followers')
        all_followers_list = sorted(all_followers_list, key=lambda x: (-x[1], -x[2]))

        ind = 2
from tkinter import filedialog
            if not login(self.username.get(), self.password.get()):
            source_sheet.cell(row=2, column=2).value = self.target_user['name']
            summary_sheet.cell(row=ind, column=3).value = value[2]
            summary_sheet.cell(row=ind, column=4).value = value[3]
            ind += 1

        book.save(output_file)
                        time.sleep(60)
                                    ind += 1
        logout()



    root = tk.Tk()
        source_sheet.cell(row=1, column=3).value = 'exclude users with follower count less than'
        self.target_user = {}
    root.mainloop()


if __name__ == '__main__':
    main()