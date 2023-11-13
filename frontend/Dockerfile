# Start from the Go builder image for compiling the source code
FROM public.ecr.aws/docker/library/golang:1.21.4 as builder

WORKDIR /go/src/app

COPY . .

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Build the Go app
RUN CGO_ENABLED=0 go build -o /go/bin/app

# Now copy it into our distroless base image
FROM gcr.io/distroless/base-debian12

COPY --from=builder /go/bin/app /

# Expose port 8001 to the outside world
EXPOSE 8001

# Command to run the executable
ENTRYPOINT ["/app"]
