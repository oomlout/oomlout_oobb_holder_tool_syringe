import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = "holder_tool"
            kwargs["oomp_color"] = "syringe"
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        #1_multiple
        heights = [3,4]        
        for hei in heights:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 5
            p3["height"] = hei
            p3["thickness"] = 3
            p3["extra"] = "tool_syringe_100_ml_1_multiple"
            part["kwargs"] = p3
            nam = "holder_tool"
            part["name"] = nam
            if oomp_mode == "oobb":
                pass
                #p3["oomp_size"] = nam
            if not test:
                pass
                parts.append(part)

        #3_multiple#
        heights = [3,4]
        for hei in heights:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 11
            p3["height"] = hei
            p3["thickness"] = 3
            p3["extra"] = "tool_syringe_100_ml_3_multiple"
            part["kwargs"] = p3
            nam = "holder_tool"
            part["name"] = nam
            if oomp_mode == "oobb":
                pass
                #p3["oomp_size"] = nam
            if not test:
                parts.append(part)

        #tip
        for hei in heights:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 1
            p3["height"] = 3
            p3["thickness"] = 18
            p3["extra"] = "tip_cover"
            part["kwargs"] = p3
            nam = "holder_tool"
            part["name"] = nam
            if oomp_mode == "oobb":
                pass
                #p3["oomp_size"] = nam
            if not test:
                parts.append(part)

        #tip lid
        for hei in heights:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 1.5
            p3["height"] = 1.5
            p3["thickness"] = 15
            p3["extra"] = "tip_lid"
            part["kwargs"] = p3
            nam = "holder_tool"
            part["name"] = nam
            if oomp_mode == "oobb":
                pass
                #p3["oomp_size"] = nam
            if not test:
                parts.append(part)

    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    if "tip_cover" in extra:
        get_tip_cover(thing, **kwargs)
    elif "tip_lid" in extra:
        get_tip_lid(thing, **kwargs)
    else:

        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_plate"    
        p3["depth"] = depth
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add holes seperate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = ["top","bottom"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #if 1_multple in extra
        #add holders
        if True:
            radius_holder = 40/2
            #if 1_multiple in extra
            if "1_multiple" in extra:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "negative"
                p3["shape"] = f"oobb_cylinder"
                p3["depth"] = depth
                p3["radius"] = radius_holder
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)     
                pos1[2] += depth/2    
                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)
            #if 3_multiple in extra
            elif "3_multiple" in extra:
                repeats = 3
                start = -(repeats-1)/2 * 45
                shift = 45
                for i in range(repeats):
                    p3 = copy.deepcopy(kwargs)
                    p3["type"] = "negative"
                    p3["shape"] = f"oobb_cylinder"
                    p3["depth"] = depth
                    p3["radius"] = radius_holder
                    p3["m"] = "#"
                    pos1 = copy.deepcopy(pos)     
                    pos1[0] += start + i * shift
                    pos1[2] += depth/2    
                    p3["pos"] = pos1
                    oobb_base.append_full(thing,**p3)


        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 50
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            pos1 = copy.deepcopy(pos)
            pos1[0] += -500/2
            pos1[1] += 0
            pos1[2] += -500/2        
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)
    
def get_tip_cover(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    
    if True:

        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = 1.5
        p3["depth"] = depth
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add holes seperate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = ["left","right"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #if 1_multple in extra
        #add holders
        if True:
            radius_holder = 10/2
            #if 1_multiple in extra
            pad = 3
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "negative"
                p3["shape"] = f"oobb_cylinder"
                p3["depth"] = depth-pad
                p3["radius"] = radius_holder
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)     
                pos1[2] += depth/2   + pad/2
                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)


        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 50
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            pos1 = copy.deepcopy(pos)
            pos1[0] += -500/2
            pos1[1] += 0
            pos1[2] += -500/2        
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

def get_tip_lid(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    
    if True:

        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_plate"            
        p3["depth"] = depth
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add holes seperate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = ["left","right"]
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        #oobb_base.append_full(thing,**p3)

        #if 1_multple in extra
        #add holders
        if True:
            radius_top = 6.5/2
            radius_bottom = 5.5/2
            #if 1_multiple in extra
            pad = 3
            if True:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "negative"
                p3["shape"] = f"oobb_cylinder"
                p3["depth"] = depth-pad
                p3["radius_2"] = radius_top
                p3["radius_1"] = radius_bottom
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)     
                pos1[2] += depth/2   + pad/2
                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)



if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)