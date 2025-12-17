namespace ToDoUtils
{
    public class Utils
    {
        // Global list of todos (equivalent to Python list)
        static List<string> todos = new List<string> { "Make a cup of tea" };

        public static void PrintTodos()
        {
            for (int i = 0; i < todos.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {todos[i]}");
            }
        }

        public static void PrintMenu()
        {
            Console.WriteLine("\nToDo Menu");
            Console.WriteLine("1. View ToDos");
            Console.WriteLine("2. Add a ToDo");
            Console.WriteLine("3. Remove a ToDo");
            Console.WriteLine("4. Exit");
        }

        public static void ListTodos()
        {
            if (todos.Count == 0)
            {
                Console.WriteLine("No ToDos!");
            }
            else
            {
                PrintTodos();
            }
        }

        public static void AddTodo()
        {
            Console.Write("Enter a new todo: ");
            string todo = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(todo))
            {
                Console.WriteLine("Entry cannot be empty!");
            }
            else
            {
                todos.Add(todo.Trim());
                Console.WriteLine("Todo added!");
            }
        }

        public static void RemoveTodo()
        {
            if (todos.Count == 0)
            {
                Console.WriteLine("No ToDos!");
                return;
            }

            PrintTodos();
            Console.Write("Enter a number to remove: ");

            if (!int.TryParse(Console.ReadLine(), out int num))
            {
                Console.WriteLine("Invalid number!");
                return;
            }

            if (num <= 0 || num > todos.Count)
            {
                Console.WriteLine("Invalid number!");
            }
            else
            {
                string removedTodo = todos[num - 1];
                todos.RemoveAt(num - 1);
                Console.WriteLine($"Removed {removedTodo} from the list");
            }
        }
    }
}
