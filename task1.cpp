#include <iostream>
using namespace std;

double celsius_to_fahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32;
}

double fahrenheit_to_celsius(double fahrenheit) {
    return (fahrenheit - 32) * 5.0 / 9.0;
}

double celsius_to_kelvin(double celsius) {
    return celsius + 273.15;
}

double kelvin_to_celsius(double kelvin) {
    return kelvin - 273.15;
}

double fahrenheit_to_kelvin(double fahrenheit) {
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit));
}

double kelvin_to_fahrenheit(double kelvin) {
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin));
}

int main() {
    char choice;
    double temperature;

    cout << "Enter the temperature: ";
    cin >> temperature;

    cout << "Enter the unit of temperature (C, F, or K): ";
    cin >> choice;

    switch(choice) {
        case 'C':
        case 'c':
            cout << temperature << " Celsius is equivalent to:" << endl;
            cout << celsius_to_fahrenheit(temperature) << " Fahrenheit" << endl;
            cout << celsius_to_kelvin(temperature) << " Kelvin" << endl;
            break;
        case 'F':
        case 'f':
            cout << temperature << " Fahrenheit is equivalent to:" << endl;
            cout << fahrenheit_to_celsius(temperature) << " Celsius" << endl;
            cout << fahrenheit_to_kelvin(temperature) << " Kelvin" << endl;
            break;
        case 'K':
        case 'k':
            cout << temperature << " Kelvin is equivalent to:" << endl;
            cout << kelvin_to_celsius(temperature) << " Celsius" << endl;
            cout << kelvin_to_fahrenheit(temperature) << " Fahrenheit" << endl;
            break;
        default:
            cout << "Invalid choice!" << endl;
    }

    return 0;
}
