
namespace WindowsFormsApp7
{
    partial class Form5
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.Windows.Forms.Label iDБронированияLabel;
            System.Windows.Forms.Label iDКлиентаLabel;
            System.Windows.Forms.Label iDТураLabel;
            System.Windows.Forms.Label iDОтеляLabel;
            System.Windows.Forms.Label датаБронированияLabel;
            System.Windows.Forms.Label датаЗаездаLabel;
            System.Windows.Forms.Label датаВыездаLabel;
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form5));
            this.дипломDataSet = new WindowsFormsApp7.дипломDataSet();
            this.бронированияBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.бронированияTableAdapter = new WindowsFormsApp7.дипломDataSetTableAdapters.БронированияTableAdapter();
            this.tableAdapterManager = new WindowsFormsApp7.дипломDataSetTableAdapters.TableAdapterManager();
            this.iDБронированияTextBox = new System.Windows.Forms.TextBox();
            this.iDКлиентаTextBox = new System.Windows.Forms.TextBox();
            this.iDТураTextBox = new System.Windows.Forms.TextBox();
            this.iDОтеляTextBox = new System.Windows.Forms.TextBox();
            this.датаБронированияDateTimePicker = new System.Windows.Forms.DateTimePicker();
            this.датаЗаездаDateTimePicker = new System.Windows.Forms.DateTimePicker();
            this.датаВыездаDateTimePicker = new System.Windows.Forms.DateTimePicker();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.BindingNavigator = new System.Windows.Forms.BindingNavigator(this.components);
            this.bindingNavigatorAddNewItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorCountItem = new System.Windows.Forms.ToolStripLabel();
            this.bindingNavigatorDeleteItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveFirstItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMovePreviousItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorPositionItem = new System.Windows.Forms.ToolStripTextBox();
            this.bindingNavigatorSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorMoveNextItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveLastItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.бронированияBindingNavigatorSaveItem = new System.Windows.Forms.ToolStripButton();
            iDБронированияLabel = new System.Windows.Forms.Label();
            iDКлиентаLabel = new System.Windows.Forms.Label();
            iDТураLabel = new System.Windows.Forms.Label();
            iDОтеляLabel = new System.Windows.Forms.Label();
            датаБронированияLabel = new System.Windows.Forms.Label();
            датаЗаездаLabel = new System.Windows.Forms.Label();
            датаВыездаLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.дипломDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.бронированияBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.BindingNavigator)).BeginInit();
            this.BindingNavigator.SuspendLayout();
            this.SuspendLayout();
            // 
            // дипломDataSet
            // 
            this.дипломDataSet.DataSetName = "дипломDataSet";
            this.дипломDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // бронированияBindingSource
            // 
            this.бронированияBindingSource.DataMember = "Бронирования";
            this.бронированияBindingSource.DataSource = this.дипломDataSet;
            // 
            // бронированияTableAdapter
            // 
            this.бронированияTableAdapter.ClearBeforeFill = true;
            // 
            // tableAdapterManager
            // 
            this.tableAdapterManager.BackupDataSetBeforeUpdate = false;
            this.tableAdapterManager.UpdateOrder = WindowsFormsApp7.дипломDataSetTableAdapters.TableAdapterManager.UpdateOrderOption.InsertUpdateDelete;
            this.tableAdapterManager.БронированияTableAdapter = this.бронированияTableAdapter;
            this.tableAdapterManager.ГидыTableAdapter = null;
            this.tableAdapterManager.КлиентыTableAdapter = null;
            this.tableAdapterManager.ОтелиTableAdapter = null;
            this.tableAdapterManager.ОтзывыTableAdapter = null;
            this.tableAdapterManager.СотрудникиTableAdapter = null;
            this.tableAdapterManager.ТурыTableAdapter = null;
            // 
            // iDБронированияLabel
            // 
            iDБронированияLabel.AutoSize = true;
            iDБронированияLabel.Location = new System.Drawing.Point(28, 35);
            iDБронированияLabel.Name = "iDБронированияLabel";
            iDБронированияLabel.Size = new System.Drawing.Size(94, 13);
            iDБронированияLabel.TabIndex = 1;
            iDБронированияLabel.Text = "IDБронирования:";
            // 
            // iDБронированияTextBox
            // 
            this.iDБронированияTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.бронированияBindingSource, "IDБронирования", true));
            this.iDБронированияTextBox.Location = new System.Drawing.Point(128, 32);
            this.iDБронированияTextBox.Name = "iDБронированияTextBox";
            this.iDБронированияTextBox.Size = new System.Drawing.Size(100, 20);
            this.iDБронированияTextBox.TabIndex = 2;
            // 
            // iDКлиентаLabel
            // 
            iDКлиентаLabel.AutoSize = true;
            iDКлиентаLabel.Location = new System.Drawing.Point(59, 76);
            iDКлиентаLabel.Name = "iDКлиентаLabel";
            iDКлиентаLabel.Size = new System.Drawing.Size(63, 13);
            iDКлиентаLabel.TabIndex = 3;
            iDКлиентаLabel.Text = "IDКлиента:";
            // 
            // iDКлиентаTextBox
            // 
            this.iDКлиентаTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.бронированияBindingSource, "IDКлиента", true));
            this.iDКлиентаTextBox.Location = new System.Drawing.Point(128, 73);
            this.iDКлиентаTextBox.Name = "iDКлиентаTextBox";
            this.iDКлиентаTextBox.Size = new System.Drawing.Size(100, 20);
            this.iDКлиентаTextBox.TabIndex = 4;
            // 
            // iDТураLabel
            // 
            iDТураLabel.AutoSize = true;
            iDТураLabel.Location = new System.Drawing.Point(77, 114);
            iDТураLabel.Name = "iDТураLabel";
            iDТураLabel.Size = new System.Drawing.Size(45, 13);
            iDТураLabel.TabIndex = 5;
            iDТураLabel.Text = "IDТура:";
            // 
            // iDТураTextBox
            // 
            this.iDТураTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.бронированияBindingSource, "IDТура", true));
            this.iDТураTextBox.Location = new System.Drawing.Point(128, 111);
            this.iDТураTextBox.Name = "iDТураTextBox";
            this.iDТураTextBox.Size = new System.Drawing.Size(100, 20);
            this.iDТураTextBox.TabIndex = 6;
            // 
            // iDОтеляLabel
            // 
            iDОтеляLabel.AutoSize = true;
            iDОтеляLabel.Location = new System.Drawing.Point(70, 140);
            iDОтеляLabel.Name = "iDОтеляLabel";
            iDОтеляLabel.Size = new System.Drawing.Size(52, 13);
            iDОтеляLabel.TabIndex = 7;
            iDОтеляLabel.Text = "IDОтеля:";
            // 
            // iDОтеляTextBox
            // 
            this.iDОтеляTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.бронированияBindingSource, "IDОтеля", true));
            this.iDОтеляTextBox.Location = new System.Drawing.Point(128, 137);
            this.iDОтеляTextBox.Name = "iDОтеляTextBox";
            this.iDОтеляTextBox.Size = new System.Drawing.Size(100, 20);
            this.iDОтеляTextBox.TabIndex = 8;
            // 
            // датаБронированияLabel
            // 
            датаБронированияLabel.AutoSize = true;
            датаБронированияLabel.Location = new System.Drawing.Point(10, 166);
            датаБронированияLabel.Name = "датаБронированияLabel";
            датаБронированияLabel.Size = new System.Drawing.Size(112, 13);
            датаБронированияLabel.TabIndex = 9;
            датаБронированияLabel.Text = "Дата Бронирования:";
            // 
            // датаБронированияDateTimePicker
            // 
            this.датаБронированияDateTimePicker.DataBindings.Add(new System.Windows.Forms.Binding("Value", this.бронированияBindingSource, "ДатаБронирования", true));
            this.датаБронированияDateTimePicker.Location = new System.Drawing.Point(128, 162);
            this.датаБронированияDateTimePicker.Name = "датаБронированияDateTimePicker";
            this.датаБронированияDateTimePicker.Size = new System.Drawing.Size(200, 20);
            this.датаБронированияDateTimePicker.TabIndex = 10;
            // 
            // датаЗаездаLabel
            // 
            датаЗаездаLabel.AutoSize = true;
            датаЗаездаLabel.Location = new System.Drawing.Point(46, 192);
            датаЗаездаLabel.Name = "датаЗаездаLabel";
            датаЗаездаLabel.Size = new System.Drawing.Size(76, 13);
            датаЗаездаLabel.TabIndex = 11;
            датаЗаездаLabel.Text = "Дата Заезда:";
            // 
            // датаЗаездаDateTimePicker
            // 
            this.датаЗаездаDateTimePicker.DataBindings.Add(new System.Windows.Forms.Binding("Value", this.бронированияBindingSource, "ДатаЗаезда", true));
            this.датаЗаездаDateTimePicker.Location = new System.Drawing.Point(128, 188);
            this.датаЗаездаDateTimePicker.Name = "датаЗаездаDateTimePicker";
            this.датаЗаездаDateTimePicker.Size = new System.Drawing.Size(200, 20);
            this.датаЗаездаDateTimePicker.TabIndex = 12;
            // 
            // датаВыездаLabel
            // 
            датаВыездаLabel.AutoSize = true;
            датаВыездаLabel.Location = new System.Drawing.Point(44, 218);
            датаВыездаLabel.Name = "датаВыездаLabel";
            датаВыездаLabel.Size = new System.Drawing.Size(78, 13);
            датаВыездаLabel.TabIndex = 13;
            датаВыездаLabel.Text = "Дата Выезда:";
            // 
            // датаВыездаDateTimePicker
            // 
            this.датаВыездаDateTimePicker.DataBindings.Add(new System.Windows.Forms.Binding("Value", this.бронированияBindingSource, "ДатаВыезда", true));
            this.датаВыездаDateTimePicker.Location = new System.Drawing.Point(128, 214);
            this.датаВыездаDateTimePicker.Name = "датаВыездаDateTimePicker";
            this.датаВыездаDateTimePicker.Size = new System.Drawing.Size(200, 20);
            this.датаВыездаDateTimePicker.TabIndex = 14;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(31, 275);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 15;
            this.button1.Text = "back";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(117, 275);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 16;
            this.button2.Text = "пред";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(212, 275);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 17;
            this.button3.Text = "след";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(310, 275);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 18;
            this.button4.Text = "обновить";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(405, 275);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(75, 23);
            this.button5.TabIndex = 19;
            this.button5.Text = "удалить";
            this.button5.UseVisualStyleBackColor = true;
            // 
            // BindingNavigator
            // 
            this.BindingNavigator.AddNewItem = this.bindingNavigatorAddNewItem;
            this.BindingNavigator.BindingSource = this.бронированияBindingSource;
            this.BindingNavigator.CountItem = this.bindingNavigatorCountItem;
            this.BindingNavigator.DeleteItem = this.bindingNavigatorDeleteItem;
            this.BindingNavigator.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bindingNavigatorMoveFirstItem,
            this.bindingNavigatorMovePreviousItem,
            this.bindingNavigatorSeparator,
            this.bindingNavigatorPositionItem,
            this.bindingNavigatorCountItem,
            this.bindingNavigatorSeparator1,
            this.bindingNavigatorMoveNextItem,
            this.bindingNavigatorMoveLastItem,
            this.bindingNavigatorSeparator2,
            this.bindingNavigatorAddNewItem,
            this.bindingNavigatorDeleteItem,
            this.бронированияBindingNavigatorSaveItem});
            this.BindingNavigator.Location = new System.Drawing.Point(0, 0);
            this.BindingNavigator.MoveFirstItem = this.bindingNavigatorMoveFirstItem;
            this.BindingNavigator.MoveLastItem = this.bindingNavigatorMoveLastItem;
            this.BindingNavigator.MoveNextItem = this.bindingNavigatorMoveNextItem;
            this.BindingNavigator.MovePreviousItem = this.bindingNavigatorMovePreviousItem;
            this.BindingNavigator.Name = "BindingNavigator";
            this.BindingNavigator.PositionItem = this.bindingNavigatorPositionItem;
            this.BindingNavigator.Size = new System.Drawing.Size(1064, 25);
            this.BindingNavigator.TabIndex = 20;
            this.BindingNavigator.Text = "bindingNavigator1";
            // 
            // bindingNavigatorAddNewItem
            // 
            this.bindingNavigatorAddNewItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorAddNewItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorAddNewItem.Image")));
            this.bindingNavigatorAddNewItem.Name = "bindingNavigatorAddNewItem";
            this.bindingNavigatorAddNewItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorAddNewItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorAddNewItem.Text = "Добавить";
            // 
            // bindingNavigatorCountItem
            // 
            this.bindingNavigatorCountItem.Name = "bindingNavigatorCountItem";
            this.bindingNavigatorCountItem.Size = new System.Drawing.Size(43, 22);
            this.bindingNavigatorCountItem.Text = "для {0}";
            this.bindingNavigatorCountItem.ToolTipText = "Общее число элементов";
            // 
            // bindingNavigatorDeleteItem
            // 
            this.bindingNavigatorDeleteItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorDeleteItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorDeleteItem.Image")));
            this.bindingNavigatorDeleteItem.Name = "bindingNavigatorDeleteItem";
            this.bindingNavigatorDeleteItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorDeleteItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorDeleteItem.Text = "Удалить";
            // 
            // bindingNavigatorMoveFirstItem
            // 
            this.bindingNavigatorMoveFirstItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveFirstItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveFirstItem.Image")));
            this.bindingNavigatorMoveFirstItem.Name = "bindingNavigatorMoveFirstItem";
            this.bindingNavigatorMoveFirstItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveFirstItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMoveFirstItem.Text = "Переместить в начало";
            // 
            // bindingNavigatorMovePreviousItem
            // 
            this.bindingNavigatorMovePreviousItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMovePreviousItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMovePreviousItem.Image")));
            this.bindingNavigatorMovePreviousItem.Name = "bindingNavigatorMovePreviousItem";
            this.bindingNavigatorMovePreviousItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMovePreviousItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMovePreviousItem.Text = "Переместить назад";
            // 
            // bindingNavigatorSeparator
            // 
            this.bindingNavigatorSeparator.Name = "bindingNavigatorSeparator";
            this.bindingNavigatorSeparator.Size = new System.Drawing.Size(6, 25);
            // 
            // bindingNavigatorPositionItem
            // 
            this.bindingNavigatorPositionItem.AccessibleName = "Положение";
            this.bindingNavigatorPositionItem.AutoSize = false;
            this.bindingNavigatorPositionItem.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.bindingNavigatorPositionItem.Name = "bindingNavigatorPositionItem";
            this.bindingNavigatorPositionItem.Size = new System.Drawing.Size(50, 23);
            this.bindingNavigatorPositionItem.Text = "0";
            this.bindingNavigatorPositionItem.ToolTipText = "Текущее положение";
            // 
            // bindingNavigatorSeparator1
            // 
            this.bindingNavigatorSeparator1.Name = "bindingNavigatorSeparator1";
            this.bindingNavigatorSeparator1.Size = new System.Drawing.Size(6, 25);
            // 
            // bindingNavigatorMoveNextItem
            // 
            this.bindingNavigatorMoveNextItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveNextItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveNextItem.Image")));
            this.bindingNavigatorMoveNextItem.Name = "bindingNavigatorMoveNextItem";
            this.bindingNavigatorMoveNextItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveNextItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMoveNextItem.Text = "Переместить вперед";
            // 
            // bindingNavigatorMoveLastItem
            // 
            this.bindingNavigatorMoveLastItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveLastItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveLastItem.Image")));
            this.bindingNavigatorMoveLastItem.Name = "bindingNavigatorMoveLastItem";
            this.bindingNavigatorMoveLastItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveLastItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMoveLastItem.Text = "Переместить в конец";
            // 
            // bindingNavigatorSeparator2
            // 
            this.bindingNavigatorSeparator2.Name = "bindingNavigatorSeparator2";
            this.bindingNavigatorSeparator2.Size = new System.Drawing.Size(6, 25);
            // 
            // бронированияBindingNavigatorSaveItem
            // 
            this.бронированияBindingNavigatorSaveItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.бронированияBindingNavigatorSaveItem.Image = ((System.Drawing.Image)(resources.GetObject("бронированияBindingNavigatorSaveItem.Image")));
            this.бронированияBindingNavigatorSaveItem.Name = "бронированияBindingNavigatorSaveItem";
            this.бронированияBindingNavigatorSaveItem.Size = new System.Drawing.Size(23, 22);
            this.бронированияBindingNavigatorSaveItem.Text = "Сохранить данные";
            // 
            // Form5
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1064, 450);
            this.Controls.Add(this.BindingNavigator);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(датаВыездаLabel);
            this.Controls.Add(this.датаВыездаDateTimePicker);
            this.Controls.Add(датаЗаездаLabel);
            this.Controls.Add(this.датаЗаездаDateTimePicker);
            this.Controls.Add(датаБронированияLabel);
            this.Controls.Add(this.датаБронированияDateTimePicker);
            this.Controls.Add(iDОтеляLabel);
            this.Controls.Add(this.iDОтеляTextBox);
            this.Controls.Add(iDТураLabel);
            this.Controls.Add(this.iDТураTextBox);
            this.Controls.Add(iDКлиентаLabel);
            this.Controls.Add(this.iDКлиентаTextBox);
            this.Controls.Add(iDБронированияLabel);
            this.Controls.Add(this.iDБронированияTextBox);
            this.Name = "Form5";
            this.Text = "Form5";
            this.Load += new System.EventHandler(this.Form5_Load);
            ((System.ComponentModel.ISupportInitialize)(this.дипломDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.бронированияBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.BindingNavigator)).EndInit();
            this.BindingNavigator.ResumeLayout(false);
            this.BindingNavigator.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private дипломDataSet дипломDataSet;
        private System.Windows.Forms.BindingSource бронированияBindingSource;
        private дипломDataSetTableAdapters.БронированияTableAdapter бронированияTableAdapter;
        private дипломDataSetTableAdapters.TableAdapterManager tableAdapterManager;
        private System.Windows.Forms.TextBox iDБронированияTextBox;
        private System.Windows.Forms.TextBox iDКлиентаTextBox;
        private System.Windows.Forms.TextBox iDТураTextBox;
        private System.Windows.Forms.TextBox iDОтеляTextBox;
        private System.Windows.Forms.DateTimePicker датаБронированияDateTimePicker;
        private System.Windows.Forms.DateTimePicker датаЗаездаDateTimePicker;
        private System.Windows.Forms.DateTimePicker датаВыездаDateTimePicker;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.BindingNavigator BindingNavigator;
        private System.Windows.Forms.ToolStripButton bindingNavigatorAddNewItem;
        private System.Windows.Forms.ToolStripLabel bindingNavigatorCountItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorDeleteItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveFirstItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMovePreviousItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator;
        private System.Windows.Forms.ToolStripTextBox bindingNavigatorPositionItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator1;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveNextItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveLastItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator2;
        private System.Windows.Forms.ToolStripButton бронированияBindingNavigatorSaveItem;
    }
}