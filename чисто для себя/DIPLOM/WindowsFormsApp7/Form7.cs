using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp7
{
    public partial class Form7 : Form
    {
        public Form7()
        {
            InitializeComponent();
        }

        private void бронированияBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.бронированияBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.дипломDataSet);

        }

        private void Form7_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "дипломDataSet.Бронирования". При необходимости она может быть перемещена или удалена.
            this.бронированияTableAdapter.Fill(this.дипломDataSet.Бронирования);

        }
    }
}
