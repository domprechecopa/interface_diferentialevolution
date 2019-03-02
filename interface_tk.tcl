#############################################################################
# Generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#  Jan 26, 2019 07:04:56 PM -03  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

vTcl:font:add_GUI_font TkDefaultFont \
"-family sans-serif -size -12 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font TkFixedFont \
"-family monospace -size -12 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font TkMenuFont \
"-family sans-serif -size -12 -weight normal -slant roman -underline 0 -overstrike 0"
vTcl:font:add_GUI_font TkTextFont \
"-family sans-serif -size -12 -weight normal -slant roman -underline 0 -overstrike 0"
set vTcl(actual_gui_font_dft_name) TkDefaultFont
set vTcl(actual_gui_font_menu_name) TkMenuFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 936x689+545+258
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra43 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 345 \
        -highlightcolor black -width 145 
    vTcl:DefineAlias "$top.fra43" "Input_Dados" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra43
    label $site_3_0.lab48 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black \
        -text {Número de Iterações} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text Dim 
    vTcl:DefineAlias "$site_3_0.lab49" "Label1_4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text CR 
    vTcl:DefineAlias "$site_3_0.lab50" "Label1_5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text F 
    vTcl:DefineAlias "$site_3_0.lab51" "Label1_6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text {Polupation Size} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label1_7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text {Upper Limit} 
    vTcl:DefineAlias "$site_3_0.lab53" "Label1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text {Lower Limit} 
    vTcl:DefineAlias "$site_3_0.lab54" "Label1_9" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text {Print Status} 
    vTcl:DefineAlias "$site_3_0.lab55" "Label1_10" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text Function 
    vTcl:DefineAlias "$site_3_0.lab56" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black -anchor sw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text {Number Runs} 
    vTcl:DefineAlias "$site_3_0.lab43" "text_num_runs" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab48 \
        -in $site_3_0 -x 10 -y 10 -width 126 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 10 -y 40 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 10 -y 70 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 10 -y 100 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 10 -y 130 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 10 -y 160 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 10 -y 190 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 10 -y 220 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 10 -y 250 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 10 -y 280 -width 86 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra57 \
        -borderwidth 2 -relief groove -background {#d9d9d9} -height 345 \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.fra57" "ent_num_runs" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra57
    entry $site_3_0.ent58 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent58" "ent_num_iter" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent59 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent59" "ent_dim" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent60 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent60" "ent_CR" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent61 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent61" "ent_F" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent62 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent62" "ent_pop_size" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent63 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent63" "ent_upper_lim" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent64 \
        -background white -font TkFixedFont -foreground {#000000} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent64" "ent_lower_lim" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che86 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -justify left -text Mostrar -variable che86 
    vTcl:DefineAlias "$site_3_0.che86" "Sel_MostrarPrint" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo44 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo44" "select_funcao" vTcl:WidgetProc "Toplevel1" 1
    spinbox $site_3_0.spi44 \
        -activebackground {#f9f9f9} -background white -font TkTextFont \
        -foreground black -from 1.0 -highlightbackground black \
        -highlightcolor black -increment 1.0 -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black \
        -textvariable spinbox -to 100.0 
    vTcl:DefineAlias "$site_3_0.spi44" "ent_num_run" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent58 \
        -in $site_3_0 -x 10 -y 10 -width 106 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent59 \
        -in $site_3_0 -x 10 -y 40 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent60 \
        -in $site_3_0 -x 10 -y 70 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent61 \
        -in $site_3_0 -x 10 -y 100 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent62 \
        -in $site_3_0 -x 10 -y 130 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent63 \
        -in $site_3_0 -x 10 -y 160 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent64 \
        -in $site_3_0 -x 10 -y 190 -width 106 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che86 \
        -in $site_3_0 -x 10 -y 220 -anchor nw -bordermode ignore 
    place $site_3_0.tCo44 \
        -in $site_3_0 -x 10 -y 250 -width 107 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.spi44 \
        -in $site_3_0 -x 10 -y 280 -width 107 -relwidth 0 -height 22 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -text {Limpar Dados} 
    vTcl:DefineAlias "$top.but43" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -state active -text Executar 
    vTcl:DefineAlias "$top.but44" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -text Plot 
    vTcl:DefineAlias "$top.but46" "Button4" vTcl:WidgetProc "Toplevel1" 1
    ttk::progressbar $top.tPr43
    vTcl:DefineAlias "$top.tPr43" "TProgressbar1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground {#f9f9f9} -activeforeground black -anchor nw \
        -background {#d9d9d9} -borderwidth 2 -font TkDefaultFont \
        -foreground {#000000} -highlightcolor black -text creditos 
    vTcl:DefineAlias "$top.lab45" "credits_text" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr46 \
        -background {#d9d9d9} -height 75 -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr46" "Scrolledlistbox1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr46.01 configure -background white \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    button $top.but48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -text {Limpar Histórico} 
    vTcl:DefineAlias "$top.but48" "Button2" vTcl:WidgetProc "Toplevel1" 1
    canvas $top.can53 \
        -background {#d9d9d9} -borderwidth 2 -closeenough 1.0 -height 391 \
        -highlightcolor black -insertbackground black -relief ridge \
        -selectbackground {#c4c4c4} -selectforeground black -width 551 
    vTcl:DefineAlias "$top.can53" "Canvas1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -text {< Prev} 
    vTcl:DefineAlias "$top.but54" "prev_grafico" vTcl:WidgetProc "Toplevel1" 1
    button $top.but55 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightcolor black -text {Next >} 
    vTcl:DefineAlias "$top.but55" "next_grafico" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra43 \
        -in $top -x 50 -y 20 -width 145 -relwidth 0 -height 345 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra57 \
        -in $top -x 190 -y 20 -width 125 -relwidth 0 -height 345 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 50 -y 370 -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 160 -y 370 -width 85 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 250 -y 370 -width 60 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tPr43 \
        -in $top -x 50 -y 410 -width 270 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 10 -y 630 -width 336 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.scr46 \
        -in $top -x 50 -y 450 -width 848 -relwidth 0 -height 165 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 780 -y 630 -anchor nw -bordermode ignore 
    place $top.can53 \
        -in $top -x 340 -y 20 -width 551 -relwidth 0 -height 391 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 500 -y 410 -width 45 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 690 -y 410 -width 45 -height 30 -anchor nw \
        -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

