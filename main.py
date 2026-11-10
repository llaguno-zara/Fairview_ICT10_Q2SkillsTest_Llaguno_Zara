from pyscript import document, display

def period(e):
    document.getElementById("output1").innerHTML = ""
    non_metal = {
        "H" : ("Hydrogen", 1, 1.008), 
        "He" : ("Helium", 2, 4.0026), 
        "C" : ("Carbon", 6, 12.011),  
        "N" : ("Nitrogen", 7, 14.007),  
        "O" : ("Oxygen", 8, 15.999),
        "F" : ("Fluorine", 9, 18.998),
        "Ne" : ("Neon", 10, 20.180),   
        "P" : ("Phosporus", 15, 30.974),  
        "S" : ("Sulfur", 16, 32.065),
        "Cl" : ("Chlorine", 17, 35.453),
        "Ar" : ("Argon", 18, 39.948), 
        "Se" : ("Selenium", 34, 78.960),
        "Br" : ("Bromine", 35, 79.904),
        "Kr" : ("Krypton", 36, 83.798), 
        "I" : ("Iodine", 53, 126.90), 
        "Xe" : ("Xenon", 54, 131.29), 
        "Re" : ("Radon", 86, 222),    
    
        }

    elements = document.getElementById("nonmetals").value
    show_ele = elements in non_metal
    elem = non_metal.get(elements,("Element not found", "-", "-"))
    lowerinput = document.getElementById("nonmetals").value
    elements = lowerinput.capitalize()
    
    result = f"""

    Symbol : {elements}<br>
    Element : {elem[0]}<br>
    AtomicNumber : {elem[1]}<br>
    AtomicMass : {elem[2]}
"""
    document.getElementById("output1").innerHTML = result
