from LS_Wolfe_Powell_with_Goldstein_Update import MdLineSearchWP
from LS_Wolfe_Powell import LineSearchWP
from DS_Newton_Method import newton
from DS_DFP_Method import DFP

start =np.array([-1, -1])
print("Running 'Newton Method', with fixed step length")
valN, ovfN, itersN, l0N = newton(start, 50, LSf='1')
print('iteration :',itersN, ', final:', valN[-1])

#print("Running 'DFP', with fixed step length")
#valxD, valD, ovfD, itersD, l0D = DFP(start, 50, LSf='1')
#print('iteration :',itersD, ', final:', valD[-1])

#print("Running 'Newton Method', with 'modified WP'")
#valN, ovfN, itersN, l0N = newton(start, LSf=MdLineSearchWP)
#print('iteration :',itersN, ', final:', valN[-1])

#print("Running 'DFP', with 'modified WP'")
#valxD, valD, ovfD, itersD, l0D = DFP(start, LSf=MdLineSearchWP)
#print('iteration :',itersD, ', final:', valD[-1])

#print("Running 'DFP' with B0=Hessian Inverse and 'modified WP'")
#valxD, valD, ovfD, itersD, l0D = DFP(start, DIH=0, LSf=MdLineSearchWP)
#print('iteration :',itersD, ', final:', valD[-1])

#print("Running 'Newton Method', with 'WP'")
#valN, ovfN, itersN, l0N = newton(start, LSf=LineSearchWP)
#print('iteration :',itersN, ', final:', valN[-1])

#print("Running 'DFP', with 'WP'")
#valxD1, valD1, ovfD1, itersD, l0D1 = DFP(start, LSf=LineSearchWP)
#print('iteration :',itersD, ', final:', valD[-1])

#print("Running 'DFP' with B0=Hessian Inverse and 'WP'")
#valxD, valD, ovfD, itersD, l0D = DFP(start, DIH=0, LSf=LineSearchWP)
#print('iteration :',itersD, ', final:', valD[-1])


