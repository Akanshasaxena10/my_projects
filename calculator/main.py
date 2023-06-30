'''Imported library'''
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import CyClockBase, ClockEvent, FreeClockEvent

'''created class'''
class MainApp(App):#class
    def build(self):#constructor-----defined all variables and functions
        ###creating variables
        self.operators = ['/','*','+','-']
        self.last_was_operator = None##default variable
        self.last_button = None#default variable
       # self.icon = "calculator.png"
        '''To create screen'''       
        main_layout = BoxLayout(orientation = 'vertical')##to create a vertical box layout
        self.solution = TextInput(background_color = 'black',foreground_color = 'red',multiline = False, halign = 'right',font_size = 55,readonly = True)###input screen to enter the numbers
        main_layout.add_widget(self.solution)###adding screen into main layout as widget.
        '''buttons-created array[] with nested array[][]'''
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','+'],
            ['.','0','C','-'],
        ]
        
        '''Adding the button layout to the screen'''
        for row in buttons:
            h_layout = BoxLayout()###created a for loop with a variable for box layout
            '''Creating different labels for buttons through nested for loop'''
            for label in row:
                button = Button(
                    text = label,
                    font_size = 30,
                    background_color = 'grey',)
                    #position_hint = {'center_x: 0.5', 'center_Y: 0.5'},)
                button.bind(on_press = self.on_button_press)##bind buttons to on_button_press *function to perform/operate.
                h_layout.add_widget(button)##'''insert button into layout'''  
            main_layout.add_widget(h_layout)  ##'''insert layout into main screen'''  
         ###create equal = button variable
        equal_button = Button(
            text = '=',
            font_size = 30,
            background_color = 'black',)
           # pos_hint = {'center_x:0.5', 'center_y: 50'},) 
        equal_button.bind(on_press = self.on_solution)  ####call and bind to on_solution *function with equal button 
        main_layout.add_widget(equal_button)##inserting equal button to main layout.
        
        return main_layout
        
        '''Functions'''###defining the functions
    
    def on_button_press(self,instance):####creating a function so that each pressed number would appear on the solution screen.
        current = self.solution.text
        button_text = instance.text
                
        if button_text == 'C' : ###defining clearing key.
            self.solution.text = ''  
        else:##nested loop
            if current and (self.last_was_operator and button_text in self.operators):##condition1
                return ####by default None if input number has another input in series
            elif current == '' and button_text in self.operators:##condition2
                return###by default none if on clear screen input is an operator(+,*,-)
            else: ##condition3
                new_text = current +button_text
                self.solution.text = new_text   
        self.last_button = button_text
        self.last_was_operator =self.last_button in self.operators
        
    def on_solution(self,instance):
        text  = self.solution.text  
        if text:
            solution = str(eval(self.solution.text))###first eval---means evaluate the first value in string mode  then result in solution.
            self.solution.text = solution
        
                         
            
        
'''calling main to run the app''' 
if __name__ == "__main__":
    app = MainApp()
    app.run() 
    
    
    ######To convert this script into working application we need to convert this python script into an application
    ####Build-user another python library to convert
    ####google colab-build dozer
    ####convert the main.py file to application file