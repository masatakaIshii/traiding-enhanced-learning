import tkinter

from bot import Action


class BotConfigView(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        bot_container = tkinter.LabelFrame(self, text="Bot configuration", padx=10, pady=5)

        action_container = tkinter.LabelFrame(bot_container, text="Actions", padx=10, pady=5)
        self.__action_buy = tkinter.Label(action_container, text="BUY", fg="#0f0", bg="#fff")
        self.__action_buy.grid(row=0, column=0, padx=10, pady=5)

        self.__action_keep = tkinter.Label(action_container, text="KEEP", fg="#555", bg="#fff")
        self.__action_keep.grid(row=0, column=1, padx=10, pady=5)

        self.__action_sell = tkinter.Label(action_container, text="SELL", fg="#00f", bg="#fff")
        self.__action_sell.grid(row=0, column=2, padx=10, pady=5)

        action_container.grid(row=0, column=0, pady=5)

        bot_configuration_container = tkinter.LabelFrame(bot_container, padx=10, pady=10)

        interval_label = tkinter.Label(bot_configuration_container, text="Interval :")
        interval_label.grid(row=0, column=0)
        self.interval_value = tkinter.Label(bot_configuration_container, text="Not yet")
        self.interval_value.grid(row=0, column=1)
        self.interval_entry = tkinter.Entry(bot_configuration_container, width=10)
        self.interval_entry.grid(row=0, column=2, padx=10)
        self.interval_save_btn = tkinter.Button(bot_configuration_container, text="Save")
        self.interval_save_btn.grid(row=0, column=3)

        nb_categories_label = tkinter.Label(bot_configuration_container, text="Number categories :")
        nb_categories_label.grid(row=1, column=0)
        self.nb_categories_value = tkinter.Label(bot_configuration_container, text="Not yet")
        self.nb_categories_value.grid(row=1, column=1, padx=10)
        self.nb_categories_entry = tkinter.Entry(bot_configuration_container, width=10)
        self.nb_categories_entry.grid(row=1, column=2, padx=10)
        self.nb_categories_save_btn = tkinter.Button(bot_configuration_container, text="Save")
        self.nb_categories_save_btn.grid(row=1, column=3)

        learning_rate_label = tkinter.Label(bot_configuration_container, text="Learning rate :")
        learning_rate_label.grid(row=2, column=0)
        self.learning_rate_value = tkinter.Label(bot_configuration_container, text="Not yet")
        self.learning_rate_value.grid(row=2, column=1)
        self.learning_rate_entry = tkinter.Entry(bot_configuration_container, width=10)
        self.learning_rate_entry.grid(row=2, column=2, padx=10)
        self.learning_rate_save_btn = tkinter.Button(bot_configuration_container, text="Save")
        self.learning_rate_save_btn.grid(row=2, column=3)

        discount_factor_label = tkinter.Label(bot_configuration_container, text="Discount factor :")
        discount_factor_label.grid(row=3, column=0)
        self.discount_factor_value = tkinter.Label(bot_configuration_container, text="Not yet")
        self.discount_factor_value.grid(row=3, column=1)
        self.discount_factor_entry = tkinter.Entry(bot_configuration_container, width=10)
        self.discount_factor_entry.grid(row=3, column=2, padx=10)
        self.discount_factor_save_btn = tkinter.Button(bot_configuration_container, text="Save")
        self.discount_factor_save_btn.grid(row=3, column=3)

        iteration_label = tkinter.Label(bot_configuration_container, text="Iteration :")
        iteration_label.grid(row=4, column=0)
        self.iteration_value = tkinter.Label(bot_configuration_container, text="Not yet")
        self.iteration_value.grid(row=4, column=1)
        self.iteration_entry = tkinter.Entry(bot_configuration_container, width=10)
        self.iteration_entry.grid(row=4, column=2, padx=10)
        self.iteration_save_btn = tkinter.Button(bot_configuration_container, text="Save")
        self.iteration_save_btn.grid(row=4, column=3)

        bot_configuration_container.grid(row=1)

        bot_container.pack(pady=5)

        self.grid(row=0, column=4, rowspan=2, padx=10, pady=5)

    def update_action_labels_depend_to_action(self, action):
        self.__reset_action_labels()
        match action:
            case Action.BUY:
                self.__action_buy["fg"] = "#fff"
                self.__action_buy["bg"] = "#0f0"
            case Action.KEEP:
                self.__action_keep["fg"] = "#fff"
                self.__action_keep["bg"] = "#555"
            case Action.SELL:
                self.__action_sell["fg"] = "#fff"
                self.__action_sell["bg"] = "#00f"
            case _:
                return

    def __reset_action_labels(self):
        self.__action_buy["fg"] = "#0f0"
        self.__action_buy["bg"] = "#fff"

        self.__action_keep["fg"] = "#555"
        self.__action_keep["bg"] = "#fff"

        self.__action_sell["fg"] = "#00f"
        self.__action_sell["bg"] = "#fff"
