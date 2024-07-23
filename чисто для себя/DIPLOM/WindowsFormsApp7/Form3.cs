using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WindowsFormsApp7
{
    public partial class Form3 : Form
    {
        string connectionString = "Data Source=DESKTOP-531NDOM;Initial Catalog=диплом;Integrated Security=True;";
        public Form3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Введите имя пользователя и пароль
            string username = textBoxUsername.Text;
            string password = textBoxPassword.Text;

            // Попытка подключения к базе данных
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                try
                {
                    connection.Open();

                    // Проверяем, есть ли пользователь с таким логином и паролем в базе данных
                    string query = "SELECT COUNT(*) FROM Пользователи WHERE Username = @Username AND Password = @Password";
                    SqlCommand command = new SqlCommand(query, connection);
                    command.Parameters.AddWithValue("@Username", username);
                    command.Parameters.AddWithValue("@Password", password);

                    int count = (int)command.ExecuteScalar();

                    if (count > 0)
                    {
                        MessageBox.Show("Подключение успешно!");

                        // Создаем экземпляр следующей формы
                        Form4 form4 = new Form4();
                        form4.Show();
                        this.Hide();
                    }
                    else
                    {
                        MessageBox.Show("Неверный логин или пароль");
                    }
                }
                catch (SqlException ex)
                {
                    MessageBox.Show("Ошибка подключения: " + ex.Message);
                }
            }

        }
    }
}
