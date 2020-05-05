#MPLAB�p��PWM�R�[�h�̎��������v���O����
#2020/5/4~�@�J���J�n


from tkinter import *
from tkinter import ttk



#UserInterface

class AutoCode_model(object):

    def __init__(self,
                destination,
                filename,
                pwm1h_value,
                pwm1l_value
                ):
        self.destination=destination
        self.filename=filename


    #�t�@�C���o��
    def File_input_output(self,destination,filename):
        filepath=str(self.destination.get())+"\\"+str(self.filename.get())+".txt"      #   GUI�Őݒ� �ۑ��� ,�t�@�C����
        print(filepath)
        text=Code_Sample()
        with open(filepath,mode="w",encoding="utf-8") as f:
            f.write(text)



def UserInterface():

    if __name__=="__main__":
        root=Tk()
        root.title("PWMCodeGenerator")
        root.resizable(False,False)
        main_frame=ttk.Frame(
            root,
            padding=10
        )
        main_frame.grid()

    # ���x���\������
        #�����ݒ�p�t���[��
        lf_initialsetting=ttk.LabelFrame(
            main_frame,
            text="Initial Setting",
            padding=(5,2)
        )
        lf_initialsetting.grid(row=0,column=0,pady=5)

        #�t�@�C����
        lbl_filename=ttk.Label(
            lf_initialsetting,
            text="FileName",
            padding=(5,2)
        )
        lbl_filename.grid(row=1,column=0,sticky=E)
    
        #�ۑ���
        lbl_destination=ttk.Label(
            lf_initialsetting,
            text="Destination",
            padding=(5,2)
        )
        lbl_destination.grid(row=2,column=0,sticky=E)

        #��H�萔�݌v�p�t���[��
        lf_circuit_design_setting=ttk.Labelframe(
            main_frame,
            text="Circuit Design Setting",
            padding=(5,2)
        )
        lf_circuit_design_setting.grid(row=3,column=0,pady=5)

        #��H����
        lbl_circuit_design=ttk.Label(
            lf_circuit_design_setting,
            text="Circuit Design",
            padding=(5,2)
        )
        lbl_circuit_design.grid(row=3,column=0,sticky=E)

        #�}�X�^�[�^�C���x�[�X���g��
        lbl_master_timebase_frequency=ttk.Label(
            lf_circuit_design_setting,
            text="Master Timebase Frequency",
            padding=(5,2)
        )
        lbl_master_timebase_frequency.grid(row=4,column=0,sticky=E)

        lbl_master_timebase_entity=ttk.Label(
        lf_circuit_design_setting,
            text="[kHz]",
            padding=(5,2)
        )
        lbl_master_timebase_entity.grid(row=4,column=2,sticky=E)

        #PWM�ݒ�
        lf_pwm_setting_init=ttk.Labelframe(
            main_frame,
            text="PWM Setting(Enabled or Disabled)",
            padding=(5,2)
        )
        lf_pwm_setting_init.grid(row=5,column=0,pady=5)



    #���͕���
        #�t�@�C����
        filename=StringVar()
        filename_entry=ttk.Entry(
            lf_initialsetting,
            textvariable=filename,
            width=50
        )
        filename_entry.grid(row=1,column=1)

        #�ۑ���
        destination=StringVar()
        destination_entry=ttk.Entry(
            lf_initialsetting,
            textvariable=destination,
            width=60
        )
        destination_entry.grid(row=2,column=1)

        #Combobox
        #��H����
        circuit_design=StringVar()
        cb_circuit_design=ttk.Combobox(
            lf_circuit_design_setting,
            textvariable=circuit_design
        )
        cb_circuit_design.bind("<<ComboboxSelected>>")
        cb_circuit_design["values"]=("Full-Bridge Inverter","Half-Bridge Inverter")
        cb_circuit_design.set("Full-Bridge Inverter")
        cb_circuit_design.grid(row=3,column=1)

        #�}�X�^�[�^�C���x�[�X�X�C�b�`���O���g��
        master_timebase_frequency=StringVar()
        master_timebase_frequency_entry=ttk.Entry(
            lf_circuit_design_setting,
            textvariable=master_timebase_frequency,
            width=10
        )
        master_timebase_frequency_entry.grid(row=4,column=1)



    #�@�\����

        #PWM1H �`�F�b�N�{�b�N�X�@�\
        def pwm1h_clicked():
            print("PWM1H=%s"%pwm1h_value.get())

        #PWM1L �`�F�b�N�{�b�N�X�@�\
        def pwm1l_clicked():
            print("PWM1L=%s"%pwm1l_value.get())

        #PWM2H �`�F�b�N�{�b�N�X�@�\
        def pwm2h_clicked():
            print("PWM2H=%s"%pwm2h_value.get())

        #PWM2L �`�F�b�N�{�b�N�X�@�\
        def pwm2l_clicked():
            print("PWM2L=%s"%pwm2l_value.get())

        #PWM1H �L�����@�������@�`�F�b�N�{�b�N�X
        pwm1h_value=StringVar()
        cb_pwm1h=ttk.Checkbutton(
            lf_pwm_setting_init,
            padding=5,
            text="PWM1H",
            onvalue="Enabled",
            offvalue="Disabled",
            variable=pwm1h_value,
            command=pwm1h_clicked
        )
        cb_pwm1h.grid(row=5,column=0)

        #PWM1L �L�����@�������@�`�F�b�N�{�b�N�X
        pwm1l_value=StringVar()
        cb_pwm1l=ttk.Checkbutton(
            lf_pwm_setting_init,
            padding=5,
            text="PWM1L",
            onvalue="Enabled",
            offvalue="Disabled",
            variable=pwm1l_value,
            command=pwm1l_clicked
        )
        cb_pwm1l.grid(row=5,column=1)

        #PWM2H �L�����@�������@�`�F�b�N�{�b�N�X
        pwm2h_value=StringVar()
        cb_pwm2h=ttk.Checkbutton(
            lf_pwm_setting_init,
            padding=5,
            text="PWM2H",
            onvalue="Enabled",
            offvalue="Disabled",
            variable=pwm2h_value,
            command=pwm2h_clicked
        )
        cb_pwm2h.grid(row=5,column=2)

        #PWM2L �L�����@�������@�`�F�b�N�{�b�N�X
        pwm2l_value=StringVar()
        cb_pwm2l=ttk.Checkbutton(
            lf_pwm_setting_init,
            padding=5,
            text="PWM2L",
            onvalue="Enabled",
            offvalue="Disabled",
            variable=pwm2l_value,
            command=pwm2l_clicked
        )
        cb_pwm2l.grid(row=5,column=3)

    #�t�@�C���o�́@�����@�֐��󂯓n��
        AutoCode_variable=AutoCode_model(destination,
                                        filename,
                                        pwm1h_value,
                                        pwm1l_value
                                        )

    # �R�[�h�o�͕���
        # �R�[�h�����{�^���@�\
        def generate_button_clicked():
            AutoCode_variable.File_input_output(destination,filename)
    #�R�[�h�����{�^��
        generate_button=ttk.Button(
            main_frame,
            text="Generate",
            command=generate_button_clicked
        )
        generate_button.grid(row=1,column=4,columnspan=2)


    # UserInterface ���s
        root.mainloop()


        


#�I�[�g�R�[�h���`�ǂݍ���
def Code_Sample():
    sample_filepath="C:\\Users\\*******\\Documents\\PWMCodeGenerator\\SampleCode.txt"
    sample_file=open(sample_filepath,mode="r",encoding="utf-8")
    sample_code=sample_file.read()
    sample_file.close()
    return sample_code







#Main
UserInterface()