using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;



namespace WindowsFormsApp7
{
    public partial class Form5 : Form
    {
        public Form5()
        {
            InitializeComponent();
        }

        private void бронированияBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.бронированияBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.дипломDataSet);

        }

        private void Form5_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "дипломDataSet.Бронирования". При необходимости она может быть перемещена или удалена.
            this.бронированияTableAdapter.Fill(this.дипломDataSet.Бронирования);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form4 form4 = new Form4();
            form4.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            BindingNavigator.MovePreviousItem.PerformClick();
        }

        private void BindingNavigator_RefreshItems(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            BindingNavigator.MoveNextItem.PerformClick();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Refreshdata();
        }
    }
}
