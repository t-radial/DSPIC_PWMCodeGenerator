#MPLAB用のPMWコードの自動生成プログラム
#2020/5/4~　開発開始
#2020/5/6  ファイル参照ボタン追加
            #class autocode_model add  and class autocode_generate add
            #if checkbox_string is "Enabled", replace code

import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox



#UserInterface
#AutoCode Model
class AutoCode_model(object):

    def __init__(self,
                autocode,
                destination,
                filename,
                ):
        self.autocode=autocode
        self.destination=destination
        self.filename=filename



    #ファイル入出力
    def File_input_output(self,autocode,destination,filename):
        filepath=str(self.destination.get())+"\\"+str(self.filename.get())+".txt" 
        print(filepath)
        with open(filepath,mode="w",encoding="utf-8") as f:
            f.write(self.autocode)


#コード生成
class AutoCode_Generate(object):
    def __init__(self,
                text,
                destination,
                filename,
                pwm1h_value,
                pwm1l_value
                ):
        self.sample_text=text
        self.destination=destination
        self.filename=filename
        self.pwm1h_value=pwm1h_value
        self.pwm1l_value=pwm1l_value

    def Generate_Code(self,
                    text,
                    destination,
                    filename,
                    pwm1h_value,
                    pwm1l_value
                    ):
        autocode=self.sample_text
        #PWM1H Enabled
        if self.pwm1h_value.get()=="Enabled":
            autocode=text.replace("IOCON1bits.PENH=0;","IOCON1bits.PENH=1;")
        #AutoCode_model宣言
        AutoCodeModel_variable=AutoCode_model(autocode,self.destination,self.filename)
        AutoCodeModel_variable.File_input_output(autocode,destination,filename)
    


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

    # ラベル表示部分
        #初期設定用フレーム
        lf_initialsetting=ttk.LabelFrame(
            main_frame,
            text="Initial Setting",
            padding=(5,2)
        )
        lf_initialsetting.grid(row=0,column=0,pady=5)

        #ファイル名
        lbl_filename=ttk.Label(
            lf_initialsetting,
            text="FileName",
            padding=(5,2)
        )
        lbl_filename.grid(row=1,column=0,sticky=E)
    
        #保存先
        lbl_destination=ttk.Label(
            lf_initialsetting,
            text="Destination",
            padding=(5,2)
        )
        lbl_destination.grid(row=2,column=0,sticky=E)

        #回路乗数設計用フレーム
        lf_circuit_design_setting=ttk.Labelframe(
            main_frame,
            text="Circuit Design Setting",
            padding=(5,2)
        )
        lf_circuit_design_setting.grid(row=3,column=0,pady=5)

        #回路方式
        lbl_circuit_design=ttk.Label(
            lf_circuit_design_setting,
            text="Circuit Design",
            padding=(5,2)
        )
        lbl_circuit_design.grid(row=3,column=0,sticky=E)

        #マスタタイムベーススイッチング周波数
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

        #PWM setting Frame
        lf_pwm_setting_init=ttk.Labelframe(
            main_frame,
            text="PWM Setting(Enabled or Disabled)",
            padding=(5,2)
        )
        lf_pwm_setting_init.grid(row=5,column=0,pady=5)



    #入力部分
        #ファイル名
        filename=StringVar()
        filename_entry=ttk.Entry(
            lf_initialsetting,
            textvariable=filename,
            width=50
        )
        filename_entry.grid(row=1,column=1)


        #保存先+参照ボタン追加(2020/5/6)
        def destination_reference_button_clicked():
            iDir=os.path.abspath(os.path.dirname(__file__))
            dir=filedialog.askdirectory(initialdir=iDir)
            destination.set(dir)

        destination_reference_button=ttk.Button(
            lf_initialsetting,
            text="Reference",
            command=destination_reference_button_clicked
        )
        destination_reference_button.grid(row=2,column=2)


        destination=StringVar()
        destination_entry=ttk.Entry(
            lf_initialsetting,
            textvariable=destination,
            width=60
        )
        destination_entry.grid(row=2,column=1)

        #Combobox
        #回路方式
        circuit_design=StringVar()
        cb_circuit_design=ttk.Combobox(
            lf_circuit_design_setting,
            textvariable=circuit_design
        )
        cb_circuit_design.bind("<<ComboboxSelected>>")
        cb_circuit_design["values"]=("Full-Bridge Inverter","Half-Bridge Inverter")
        cb_circuit_design.set("Full-Bridge Inverter")
        cb_circuit_design.grid(row=3,column=1)

        #マスタタイムベーススイッチング周波数
        master_timebase_frequency=StringVar()
        master_timebase_frequency_entry=ttk.Entry(
            lf_circuit_design_setting,
            textvariable=master_timebase_frequency,
            width=10
        )
        master_timebase_frequency_entry.grid(row=4,column=1)



    #PWM CheckBox

        #PWM1H Enable or Disable print
        def pwm1h_clicked():
            print("PWM1H=%s"%pwm1h_value.get())

        #PWM1L Enable or Disable print
        def pwm1l_clicked():
            print("PWM1L=%s"%pwm1l_value.get())

        #PWM2H Enable or Disable print
        def pwm2h_clicked():
            print("PWM2H=%s"%pwm2h_value.get())

        #PWM2L Enable or Disable print
        def pwm2l_clicked():
            print("PWM2L=%s"%pwm2l_value.get())

        #PWM1H  CheckBox
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

        #PWM1L CheckBox
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

        #PWM2H CheckBox
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

        #PWM2L CheckBox
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

    #雛形読み込み
        sample_text=Code_Sample()

    #AutoCode 引数宣言
        AutoCode_Generate_variable=AutoCode_Generate(sample_text,
                                                    destination,
                                                    filename,
                                                    pwm1h_value,
                                                    pwm1l_value
                                                    )
    #機能部分

        # GenerateButton Click Action
        def generate_button_clicked():
            AutoCode_Generate_variable.Generate_Code(sample_text,
                                                    destination,
                                                    filename,
                                                    pwm1h_value,
                                                    pwm1l_value    
                                                    )

        # Generate Button 
        generate_button=ttk.Button(
            main_frame,
            text="Generate",
            command=generate_button_clicked
        )
        generate_button.grid(row=1,column=4,columnspan=2)


    # UserInterface 
        root.mainloop()


        


#Code sample read action
def Code_Sample():
    iDir=os.path.abspath(os.path.dirname(__file__))
    sample_filepath=iDir+"\\SampleCode.txt"
    sample_file=open(sample_filepath,mode="r",encoding="utf-8")
    sample_code=sample_file.read()
    sample_file.close()
    return sample_code






#Main
UserInterface()