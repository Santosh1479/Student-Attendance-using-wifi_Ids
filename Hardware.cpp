#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// Replace with your network credentials
const char* ssid = "ESP8266_AP";
const char* password = "your-password";

// Server configuration
const char* serverUrl = "http://";
const char* branch = "your-branch";
const char* semester = "your-semester";
const int interval = 5000;

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);

  Serial.println("Access Point started");
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());
}

void sendStudentId(const String& studentId) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = String(serverUrl) + "/" + branch + "/" + semester + "/id";
    http.begin(url);
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"student_id\":\"" + studentId + "\"}";
    int httpResponseCode = http.POST(payload);

    if (httpResponseCode == 200) {
      Serial.println("Student ID sent successfully.");
    } else {
      Serial.print("Failed to send Student ID. Error: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi not connected");
  }
}

void loop() {
  // Scan for connected devices
  struct station_info *station_list = wifi_softap_get_station_info();
  while (station_list != NULL) {
    String studentId = String(station_list->bssid[0], HEX) + ":" +
                       String(station_list->bssid[1], HEX) + ":" +
                       String(station_list->bssid[2], HEX) + ":" +
                       String(station_list->bssid[3], HEX) + ":" +
                       String(station_list->bssid[4], HEX) + ":" +
                       String(station_list->bssid[5], HEX);
    Serial.println("Connected device: " + studentId);
    sendStudentId(studentId);
    station_list = STAILQ_NEXT(station_list, next);
  }
  wifi_softap_free_station_info();

  delay(interval);
}