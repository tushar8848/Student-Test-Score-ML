from numpy import *



def step_gradient(b_current, m_current, learning_rate):
	#gradient descent 

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	b = starting_b
	m = starting_m


	for i in range(num_iterations):
		b, m = step_gradient(b,m,array(points), learning_rate)
	return [b,m]	

def run():
	points = genfromtext('data.csv', delimeter=',')
	#hyperparameters
	learning_rate = 0.0001
	#y = mx + b (slope formula)

	initial_b = 0
	initial_m = 0
	# iterations are 1000 because of small dataset
	num_iterations = 1000
	[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	print(b)
	print(m)


if_name_ = '_main_':
	run()
