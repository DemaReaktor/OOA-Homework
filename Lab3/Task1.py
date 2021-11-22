import json
from datetime import *
import os.path


class Date:
    """date class for watching and operating date"""
    def __init__(self, *args):
        if len(args) == 3:
            date_new = date(args[0], args[1], args[2])
        else:
            date_new = date(args[0]['year'], args[0]['month'], args[0]['day'])
        self.year = date_new.year
        self.month = date_new.month
        self.day = date_new.day

    @classmethod
    def today(cls):
        """return date of today"""
        return date.today()

    def toordinal(self):
        """return a count of ended days since 1970"""
        return date(self.year, self.month, self.day).toordinal()


class FileClass:
    """class which have a date and a dictionary of events, need to write and read information of file"""
    def __init__(self, file_date, file_events):
        self.file_date = file_date
        self.file_events = file_events


class ITEvent:
    """Event"""
    __types_of_tickets = set()
    # __pers_cent_of_tickets = {}

    def __init__(self, name, date_event, price):
        self.add_type_of_ticket(StudentTicket)
        self.add_type_of_ticket(AdvancedTicket)
        self.add_type_of_ticket(LateTicket)
        if not isinstance(date_event, Date):
            raise TypeError('date_event should have type "Date"')
        if not isinstance(price, float):
            raise TypeError('price should have type "float"')
        if not isinstance(name, str):
            raise TypeError('name should have type "str"')
        if not name:
            raise ValueError('name should not have value "None"')
        if price <= 0:
            raise ValueError('price should be more 0')
        # self.get_type_from_date()
        self.__name = name
        self.__date = date_event
        self.__price = price
        self.__tickets = []

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def date(self):
        return self.__date

    @property
    def days_before_event(self):
        return self.__date.toordinal()-Date.today().toordinal()

    def create_ticket(self, for_student):
        """create ticket which is for this event and has argument is_student"""
        self.__tickets.append(self.get_type(is_student=for_student, days=self.days_before_event)(self))

    # def date_value(self):
    #     """:returns
    #     2: if 60 or more days before
    #     1: if more 10 and less 60 days before
    #     -1: if less 10 days before
    #     0: if event has ended"""
    #     time_before_event = self.__date.toordinal() - date.today().toordinal()
    #     if time_before_event >= 60:
    #         return 2
    #     if time_before_event >= 10:
    #         return 1
    #     if time_before_event >= 0:
    #         return -1
    #     return 0
    
    # def get_type_from_date(self):
    #     """return a type of ticket depending on days before event
    #     return ValueError if event has ended"""
    #     value = self.date_value()
    #     if value:
    #         return Ticket if value == 1 else (AdvancedTicket if value == 2 else LateTicket)
    #     raise ValueError('Event already has taken place')

    def show_tickets(self):
        """show count of tickets of this event"""
        count_of_student_tickets = 0
        for ticket in self.__tickets:
            if isinstance(ticket, StudentTicket):
                count_of_student_tickets += 1
        return 'usual tickets: ' + str(len(self.__tickets)-count_of_student_tickets) + ', student tickets: ' \
            + str(count_of_student_tickets)

    def show_information(self):
        """show information about event"""
        return 'ITEvent:{name: ' + self.name + ', date: ' + str(self.date.day) + str(self.date.month) + '.' + \
            str(self.date.year) + ', count of tickets: ' + '.' + str(len(self.__tickets)) + '}'

    def update_tickets(self):
        """change types of tickets depending on days before event"""
        tickets_new = []
        type_of_tickets = self.get_type(days=self.days_before_event)
        for ticket in self.__tickets:
            if isinstance(ticket, StudentTicket) or isinstance(ticket, type_of_tickets):
                tickets_new.append(ticket)
            else:
                del element
                tickets_new.append(type_of_tickets(self))
        self.__tickets = tickets_new

    def remove(self, for_student):
        """delete ticket
        return 1 if ticket was deleted
        and 0 if tickets are not"""
        if len(self.__tickets):
            for ticket in self.__tickets:
                if isinstance(ticket, StudentTicket) == for_student:
                    self.__tickets.remove(ticket)
                    return 1
        return 0

    def add(self, ticket):
        """add to this event a ticket"""
        self.__tickets.append(ticket)

    @classmethod
    def add_type_of_ticket(cls, type_of_ticket):
        if not isinstance(type_of_ticket, type):
            raise TypeError('type_of_ticket should be a "type"')
        if not issubclass(type_of_ticket, Ticket):
            raise TypeError('type_of_ticket should be son of type "Ticket"')
        cls.__types_of_tickets.add(type_of_ticket)

    @classmethod
    def get_type(cls, **kwargs):
        for element in cls.__types_of_tickets:
            if element.is_type(**kwargs):
                return element
        return Ticket if Ticket.is_type(**kwargs) else None


class Ticket:
    """usual ticket"""
    __tickets = {}
    # __PER_CENT_OF_PRICE = 1.

    def __init__(self, *args):
        if len(args) == 1:
            if not isinstance(args[0], ITEvent):
                raise TypeError('event should have type "ITEvent"')
            if not args[0]:
                raise ValueError('event should not have value "None"')
            self.__price = args[0].price
            for index in range(0, len(Ticket.__tickets)):
                if not(index in Ticket.__tickets):
                    self.__number = index
                    Ticket.__tickets[index] = self.price
                    return
            self.__number = len(Ticket.__tickets)
            Ticket.__tickets[self.__number] = self.price
            self.__event = args[0].name
        else:
            self.__number = int(args[0])
            self.__price = float(args[1])
            self.__event = args[2]

    @property
    def number(self):
        return self.__number

    @property
    def price(self):
        return self.__price*Ticket.read_per_cent(Ticket)

    @property
    def event(self):
        return self.__event

    @classmethod
    def tickets(cls):
        return cls.__tickets

    def __str__(self):
        return "ticket:{number: "+str(self.__number)+", price: "+str(self.__price)+"}"

    def __del__(self):
        if self.number in Ticket.__tickets:
            Ticket.__tickets.pop(self.number)

    @classmethod
    def show_ticket(cls, number):
        """show ticket which has this number"""
        return str(cls.__tickets[number])

    @classmethod
    def is_type(cls, **kwargs):
        return 1 if 'days' in kwargs.keys() and kwargs['days'] > 0 else 0

    @classmethod
    def read_per_cent(cls, type_of_ticket):
        with open('consts.json', 'r') as f:
            return json.loads()[type_of_ticket]


class StudentTicket(Ticket):
    """ticket for students"""

    def __init__(self, event):
        ITEvent.add_type_of_ticket(StudentTicket)
        super().__init__(event)

    @property
    def price(self):
        return self.__price * Ticket.read_per_cent(StudentTicket)

    def __str__(self):
        return "{number: "+str(self.number)+", price: "+str(self.price)+"}"

    @classmethod
    def is_type(cls, **kwargs):
        return 'is_student' in kwargs.keys() and kwargs['is_student']


class AdvancedTicket(Ticket):
    """ticket of event which will start across 60 or more days"""

    def __init__(self, event):
        ITEvent.add_type_of_ticket(self.__class__)
        super().__init__(event)

    @property
    def price(self):
        return self.__price * Ticket.read_per_cent(AdvancedTicket)

    def __str__(self):
        return "{number: "+str(self.number)+", price: "+str(self.price)+"}"

    @classmethod
    def is_type(cls, **kwargs):
        return 'days' in kwargs.keys() and kwargs['days'] >= 60


class LateTicket(Ticket):
    """ticket of event which will start across 10 or less days"""

    def __init__(self, event):
        ITEvent.add_type_of_ticket(self.__class__)
        super().__init__(event)

    @property
    def price(self):
        return self.__price * Ticket.read_per_cent(LateTicket)

    def __str__(self):
        return "{number: "+str(self.number)+", price: "+str(self.price)+"}"

    @classmethod
    def is_type(cls, **kwargs):
        return 'days' in kwargs.keys() and 10 > kwargs['days'] > 0


def file_class_encoder(obj):
    """function for reading file_class in file
    return FileClass"""
    if 'file_date' in obj:
        file_date = Date(obj['file_date'])
        file_events = {}
        for event in obj['file_events'].values():
            event_class = ITEvent(event['_ITEvent__name'], Date(event['_ITEvent__date']), event['_ITEvent__price'])
            for ticket in event['_ITEvent__tickets']:
                event_class.add(Ticket(ticket['_Ticket__number'], ticket['_Ticket__price'], ticket['_Ticket__event']))
            file_events[event_class.name] = event_class
        return FileClass(file_date, file_events)
    return obj


def read(file_name):
    """read information of file"""
    with open(file_name, 'r') as read_file:
        global events
        file_class = json.loads(read_file.read(), object_hook=file_class_encoder)
        file_date = Date(file_class.file_date.year, file_class.file_date.month, file_class.file_date.day)
        events = file_class.file_events
        if file_date.toordinal() != date.today().toordinal():
            update_events()
            for event in events.value():
                event.update_tickets()


def write(file_name):
    """write information to file"""
    with open(file_name, 'w') as write_file:
        file_class = FileClass(Date(date.today().year, date.today().month, date.today().day), events)
        write_file.write(json.dumps(file_class, default=lambda o: o.__dict__, indent=3))


def show_events():
    """show all events"""
    string = ''
    for name in events.keys():
        string += events[name].show_information() + '\n'
    return string


def buy(event, for_student):
    """buy a ticket and delete It"""
    if event.remove(for_student):
        return 'ticket was bought'
    return 'tickets were sold'


def update_events():
    """delete events which have ended"""
    global events
    events_new = {}
    for name in events.keys():
        if events[name].date():
            events_new[name] = events[name]
    events = events_new


events = {}
file_path = 'shop.json'
if os.path.isfile(file_path):
    read(file_path)
is_admin = False
is_student = False
sentence = 'commands: {show events},{show tickets: <name of event>},{buy ticket: <name of event>},'
print(sentence+'{exit},{is student},{is not student}')
while True:
    command = input()
    if command == 'show events':
        print(show_events())
    elif command == 'show ticket' and is_admin:
        print('<number>')
        Ticket.show_ticket(int(input()))
    elif command == 'add ticket' and is_admin:
        print('<event.name> <is_student>')
        sentence = input()
        events[sentence].create_ticket(input())
        write(file_path)
        print('+')
    elif command == 'add event' and is_admin:
        print('<name> <year> <month> <day> <price>')
        sentence = input()
        events[sentence] = ITEvent(sentence, Date(int(input()), int(input()), int(input())), float(input()))
        write(file_path)
        print('+')
    elif command == 'admin':
        is_admin = True
        print('+ {add ticket},{add event},{show ticket}')
    elif command == 'is not student':
        print('+')
        is_student = False
    elif command == 'is student':
        print('+')
        is_student = True
    elif command == 'exit':
        exit()
    elif not command.find('show tickets: '):
        is_event = False
        for element in events.keys():
            if element == command.replace('show tickets: ', ''):
                print(events[element].show_tickets())
                is_event = True
        if not is_event:
            print('this event was not found')
    elif not command.find('buy ticket: '):
        is_event = False
        for element in events.keys():
            if element == command.replace('buy ticket: ', ''):
                print(buy(events[element], is_student))
                write(file_path)
                is_event = True
        if not is_event:
            print('this event was not found')
    else:
        print('unknown command')
