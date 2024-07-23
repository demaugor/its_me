
namespace WindowsFormsApp7
{
    partial class Form7
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
            this.дипломDataSet = new WindowsFormsApp7.дипломDataSet();
            this.бронированияBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.бронированияTableAdapter = new WindowsFormsApp7.дипломDataSetTableAdapters.БронированияTableAdapter();
            this.tableAdapterManager = new WindowsFormsApp7.дипломDataSetTableAdapters.TableAdapterManager();
            ((System.ComponentModel.ISupportInitialize)(this.дипломDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.бронированияBindingSource)).BeginInit();
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
            // Form7
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Name = "Form7";
            this.Text = "Form7";
            this.Load += new System.EventHandler(this.Form7_Load);
            ((System.ComponentModel.ISupportInitialize)(this.дипломDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.бронированияBindingSource)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private дипломDataSet дипломDataSet;
        private System.Windows.Forms.BindingSource бронированияBindingSource;
        private дипломDataSetTableAdapters.БронированияTableAdapter бронированияTableAdapter;
        private дипломDataSetTableAdapters.TableAdapterManager tableAdapterManager;
    }
}