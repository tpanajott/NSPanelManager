#include <MqttLog.h>

void MqttLog::init(PubSubClient *mqttClient, std::string *mqttLogTopic)
{
    MqttLog::instance = this;
    this->_mqttClient = mqttClient;
    this->_mqttLogTopic = mqttLogTopic;
    this->_messageBuild = "";
    this->_messageBuilderMutex = xSemaphoreCreateMutex();

    Serial.println("MqttLog initialized.");
}

void MqttLog::setLogLevel(MqttLogLevel logLevel)
{
    Serial.print("MqttLog setting log level to ");
    Serial.println(static_cast<int>(this->_logLevel));
    LOG_INFO("Setting log level to", static_cast<int>(this->_logLevel));
    this->_logLevel = logLevel;
}