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
    public partial class Form6 : Form
    {
        public Form6()
        {
            InitializeComponent();
        }

        private void гидыBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.гидыBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.дипломDataSet);

        }

        private void Form6_Load(object sender, EventArgs e)
        {
            // TODO: данная строка кода позволяет загрузить данные в таблицу "дипломDataSet.Гиды". При необходимости она может быть перемещена или удалена.
            this.гидыTableAdapter.Fill(this.дипломDataSet.Гиды);

        }
    }
}
