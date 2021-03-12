  
 --------------------------------------------
 Physics Parameters:
 -------------------
    gravity:   9.8100000000000005     
    density water:   1025.0000000000000     
    density air:   1.1499999999999999     
    ambient pressure:   101300.00000000000     
    earth_radius:   6367500.0000000000     
    coordinate_system:           2
    sea_level:   0.0000000000000000     
  
    coriolis_forcing: T
    theta_0:   0.0000000000000000     
    friction_forcing: T
    manning_coefficient:   2.5000000000000001E-002
    friction_depth:   10000000000.000000     
  
    dry_tolerance:   1.0000000000000000E-002
  
 --------------------------------------------
 Refinement Control Parameters:
 ------------------------------
    wave_tolerance:   1.0000000000000000     
    speed_tolerance:   1.0000000000000000        2.0000000000000000        3.0000000000000000        4.0000000000000000     
    maxleveldeep:           4
    depthdeep:   300.00000000000000     
    Variable dt Refinement Ratios: T
 
  
 --------------------------------------------
 SETDTOPO:
 -------------
    num dtopo files =            0
  
 --------------------------------------------
 SETTOPO:
 ---------
    mtopofiles =            1
    
    /home/anaca/clawpack_src/clawpack-v5.7.1/geoclaw/noel_topo/topo_for_noel.tt3                                                                          
   itopotype =            3
   minlevel, maxlevel =            1           5
   tlow, thi =   -259200.00000000000        432000.00000000000     
   mx =          368   x = (  -89.833299319727885      ,  -28.616700680274079      )
   my =          306   y = (   12.966666666666660      ,   63.800000000000395      )
   dx, dy (meters/degrees) =   0.16680272108843000       0.16666666666666799     
  
   Ranking of topography files  finest to coarsest:            1
  
  
 --------------------------------------------
 SETQINIT:
 -------------
   qinit_type = 0, no perturbation
  
 --------------------------------------------
 Multilayer Parameters:
 ----------------------
    check_richardson: T
    richardson_tolerance:  0.94999999999999996     
    eigen_method:           4
    inundation_method:           2
    dry_tolerance:   1.0000000000000000E-002
