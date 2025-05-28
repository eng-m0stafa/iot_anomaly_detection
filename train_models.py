import torch
import torch.nn as nn
import numpy as np
from models import EnhancedAutoencoder, EnhancedLSTM, EnhancedDLRM, EnhancedRNN
import os

# Create sample data for training
def generate_sample_data(n_samples=1000, input_dim=10):
    # Generate normal data
    normal_data = np.random.normal(0, 1, (n_samples, input_dim))
    return torch.FloatTensor(normal_data)

# Training function
def train_model(model, data, epochs=100):
    optimizer = torch.optim.Adam(model.parameters())
    criterion = nn.MSELoss()
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, data)
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Create and train models
input_dim = 10  # Adjust based on your needs
n_samples = 1000

# Generate sample data
data = generate_sample_data(n_samples, input_dim)

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Train and save Autoencoder
print("Training Autoencoder...")
autoencoder = EnhancedAutoencoder(input_dim)
train_model(autoencoder, data)
torch.save(autoencoder.state_dict(), 'models/enhanced_autoencoder.pth')

# Train and save LSTM
print("Training LSTM...")
lstm = EnhancedLSTM(input_dim)
train_model(lstm, data)
torch.save(lstm.state_dict(), 'models/enhanced_lstm.pth')

# Train and save DLRM
print("Training DLRM...")
dlrm = EnhancedDLRM(input_dim)
train_model(dlrm, data)
torch.save(dlrm.state_dict(), 'models/enhanced_dlrm.pth')

# Train and save RNN
print("Training RNN...")
rnn = EnhancedRNN(input_dim)
train_model(rnn, data)
torch.save(rnn.state_dict(), 'models/enhanced_rnn.pth')

print("All models trained and saved successfully!")
