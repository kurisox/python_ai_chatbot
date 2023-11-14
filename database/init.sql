
#creates ServiceRequest table
CREATE TABLE ServiceRequest
(
    serviceRequestID    int             not null auto_increment,
    discordUserID       int             not null,
    processStatusID     int             not null,
    requestType         varchar(255)    not null,
    requestTitle        varchar(255)    not null,
    requestText         varchar(1024)   not null,
    PRIMARY KEY (serviceRequestID)
);

#creates Customer table
CREATE TABLE Customer
(
    customerID          int             not null auto_increment,
    discordUserID       int             not null,
    discordUserName     varchar(255),
    PRIMARY KEY (customerID)
);

#creates ProcessStatus table
CREATE TABLE ProcssStatus
(
    processStatusID     int             not null auto_increment,
    processStatusType   varchar(255)    not null,
    PRIMARY KEY (processStatusID)
);

#creates process status types
INSERT INTO ProcssStatus(processStatusType)
VALUES ('Anfrage eingegangen');
INSERT INTO ProcssStatus(processStatusType)
VALUES ('Anfrage in Bearbeitung');
INSERT INTO ProcssStatus(processStatusType)
VALUES ('Bearbeitung abgeschlossen');