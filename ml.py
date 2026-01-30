import mlflow

# =========================
# 1. 実験開始
# =========================
with mlflow.start_run():

    # ---------------------
    # パラメータ（設定値）
    # ---------------------
    lr = 0.1
    epochs = 10

    mlflow.log_param("learning_rate", lr)
    mlflow.log_param("epochs", epochs)

       # ---------------------
    # ダミーの「学習処理」
    # ---------------------
    loss = 1.0
    for epoch in range(epochs):
        loss *= 0.8  # 適当に良くなったことにする

    # ---------------------
    # メトリクス（結果）
    # ---------------------
    mlflow.log_metric("final_loss", loss)

    # ---------------------
    # アーティファクト（成果物）
    # ---------------------
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"final_loss: {loss}")

    mlflow.log_artifact("result.txt")