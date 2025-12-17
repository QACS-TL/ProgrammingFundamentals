using System;
using System.Collections.Generic;
using ToDoUtils;

class Program
{


    static void Main()
    {
        Utils.LoadTodos();
        while (true)
        {
            Utils.PrintMenu();
            Console.Write("Enter your choice: ");
            string choice = Console.ReadLine();

            if (choice == "1")
            {
                Utils.ListTodos();
            }
            else if (choice == "2")
            {
                Utils.AddTodo();
                Utils.SaveTodos();
            }
            else if (choice == "3")
            {
                Utils.RemoveTodo();
                Utils.SaveTodos();
            }
            else if (choice == "4")
            {
                Utils.SaveTodos();
                Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("\nInvalid choice");
            }
        }
    }

 
    
}
