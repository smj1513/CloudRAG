#!/bin/bash

# 환경 변수 확인
if [ -z "$AWS_ACCOUNT_ID" ] || [ -z "$AWS_REGION" ]; then
    echo "Error: AWS_ACCOUNT_ID and AWS_REGION must be set"
    exit 1
fi

# ECR 로그인
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# 이미지 빌드 및 푸시
docker build -t cloudrag-app .
docker tag cloudrag-app:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/cloudrag-app:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/cloudrag-app:latest

# ECS 서비스 업데이트
aws ecs update-service --cluster cloudrag-cluster --service cloudrag-service --force-new-deployment 