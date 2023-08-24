 

source .env

cat <<EOF > deployment.yml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: postgres-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: "/mnt/data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: imageboard-db
  labels:
    app: $DATABASE_APP
spec:
  replicas: 1
  selector:
    matchLabels:
      app: $DATABASE_APP
  template:
    metadata:
      labels:
        app: $DATABASE_APP
    spec:
      containers:
      - name: $DATABASE_IMAGE_NAME
        image: $IMAGE_TAG:$DATABASE_IMAGE_NAME
        ports: 
        - containerPort: $DATABASE_PORT
        env:
        - name: POSTGRES_DB
          value: $DATABASE_NAME
        - name: POSTGRES_USER
          value: $DATABASE_USERNAME
        - name: POSTGRES_PASSWORD
          value: $DATABASE_PASSWORD
        imagePullPolicy: Always
        volumeMounts:
          - name: postgres-persistent-storage
            mountPath: /var/lib/postgresql
      volumes:
        - name: postgres-persistent-storage
          persistentVolumeClaim:
            claimName: postgres-pv-claim
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: imageboard-app
  labels:
    app: $IMAGEBOARD_APP
spec:
  replicas: 1
  selector:
    matchLabels:
      app: $IMAGEBOARD_APP
  template:
    metadata:
      labels:
        app: $IMAGEBOARD_APP
    spec:
      containers:
      - name: $IMAGEBOARD_CONTAINER_NAME
        image: $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME
        imagePullPolicy: Always
        envFrom:
        - configMapRef:
            name: $ENVIRONMENT_NAME
        ports:
          - containerPort: $IMAGEBOARD_PORT
        volumeMounts:
          - name: postgres-persistent-storage
            mountPath: /var/lib/postgresql
      volumes:
        - name: postgres-persistent-storage
          persistentVolumeClaim:
            claimName: postgres-pv-claim
---
apiVersion: v1
kind: Service
metadata:
  name: $IMAGEBOARD_SERVICE_NAME
  labels:
    app: $IMAGEBOARD_SERVICE_NAME
spec:
  type: NodePort
  selector:
    app: $IMAGEBOARD_APP
  ports:
  - port: $IMAGEBOARD_PORT
    targetPort: $IMAGEBOARD_PORT
    nodePort: $SERVICE_PORT
    protocol: TCP

---
apiVersion: v1
kind: Service
metadata:
  name: $DATABASE_SERVICE_NAME
spec:
  selector:
    app: $DATABASE_APP
  ports:
    - protocol: TCP
      port: $DATABASE_PORT 
      targetPort: $DATABASE_PORT
  type: ClusterIP 
EOF