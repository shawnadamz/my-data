#our training data (x is the input, y_true is the actual correct answer)
x = [1, 2, 3, 4, 5]
y_true = [12, 24, 36, 48, 50] # the hidden rule is y = 2 * x

# 1. start with a completely random guess for our "weight"
weight = 0.5
learning_rate = 0.001 # how big of the step we take to fix mistakes
print("starting training.....")

# the training loop (Epochs)
for epoch in range (100):
  total_error = 0
  for i in range(len(x)):
      # make a prediction using the current weight
    y_pred = x[i] * weight

     # calculate the error (how far off were we?)
    error = y_true[i] - y_pred
    total_error += abs(error)

    # adjust the weight slightly based on the error direction
    weight += error * x[i] * learning_rate

    # print progress every 20 steps
  if epoch % 20 == 0:
          print(f"Epoch {epoch}: Current weight Guess = {weight:.4f}, Total Error = {total_error:.4f}")
          print ("\nTraining Complete!")
          print (f"the model learned that the multiplier is roughly: {weight:.2f} ")
          print (f"prediction for x=10: {10 * weight:.2f} (should be 20)")