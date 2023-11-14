FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 8005

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["PriceAPI.csproj", "./"]
RUN dotnet restore "./PriceAPI.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "PriceAPI.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "PriceAPI.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "PriceAPI.dll"]
