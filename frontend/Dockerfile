# Start from the Go builder image for compiling the source code
FROM golang:1.17 as builder

WORKDIR /app

# Copy go mod and sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source from the current directory to the Working Directory in the container
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main .

# Now copy it into our distroless base image
FROM gcr.io/distroless/base-debian12

COPY --from=builder /app/main /app/main

# Expose port 8001 to the outside world
EXPOSE 8001

# Command to run the executable
ENTRYPOINT ["/app/main"]
