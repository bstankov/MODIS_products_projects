




if __name__ == '__main__':
    from MOD_proc_functs import proces_HDF

    #path = 'C:/_LOCALdata/prj_2021/SNOW_modis/total/MOD10A2_hdf'
   #let's proces MOD10A2 files
    #
    #obj = proces_HDF()
    # # go in to path folder
    # obj.proc_MOD10A2_HDF( path)
    # # clean 10tm directory
    # obj = None
    #processing MOD10A1
    print("Now processing MOD10A1.....")
    # path_MOD10A1 = "C:/_LOCALdata/prj_2021/SNOW_modis/total/MOD10A1_hdf"
    # print("now work on creating AB snow cover")
    # obj_A1=proces_HDF()
    # obj_A1.proc_MOD10A1_HDF(path_MOD10A1)
    # # clean 10tm directory
    # obj_A1 = None
    #**********************************************
    # 1. process band reflectance data
    # path_MOD09 = "C:/_LOCALdata/prj_2021/SNOW_modis/total/MOD09A1_hdf"
    # #create a class object
    # obj_9 = proces_HDF()
    # obj_9.proc_MOD09_HDF(path_MOD09)
    # obj_9 = None
    # path_MOD35 = "C:/_LOCALdata/prj_2021/SNOW_modis/total/MOD35_hdf"
    # #create a class object
    # cloud = proces_HDF()
    # #run the function(method) against the object
    # cloud.proc_MOD35_HDF(path_MOD35 )
    # cloud = None

    # #proces for surface temperature
    # path_MOD11 = "C:/_LOCALdata/prj_2021/SNOW_modis/total/MOD11_hdf"
    # stemp = proces_HDF()
    # stemp.proc_MOD11_HDF( path_MOD11)
    # stemp = None

    #2.  process daily cloud-gap-filled (CGF) version
    #path_MOD10A1F = "C:/_LOCALdata/prj_2021/SNOW_modis/total/MYD10A1F_hdf"
    path_MOD10A1F = "U:/RS_Task_Workspaces/NDSI/2021_03_04"
    cfg = proces_HDF()
    cfg.proc_MOD10A1F_HDF(path_MOD10A1F)
    cfg = None
