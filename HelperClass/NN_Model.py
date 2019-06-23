def build_model():
    import keras
    import tensorflow as tf
    from keras.models import Sequential
    from keras.layers import Dense, Activation, Dropout

    
    model = Sequential()
    model.add(Dense(10, activation='relu', input_dim=7))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation='relu'))
    model.add(Dropout(0.10))
    model.add(Dense(5, activation='relu'))
    model.add(Dropout(0.05))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
