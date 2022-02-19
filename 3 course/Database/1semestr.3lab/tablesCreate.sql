create database Bank;
use Bank;

create table EmploymentTypes(
	employmentTypesId int unsigned primary key auto_increment,
	employmentTypesName varchar(50) not null unique
);

create table Clients(
	clientsId int unsigned primary key auto_increment,
	clientSurname varchar(30) not null,
	clientName varchar(30) not null,
	clientPatronymic varchar(30),
	passport int unsigned not null unique,
	typeOfEmployment int unsigned not null,
	foreign key (typeOfEmployment) references EmploymentTypes (employmentTypesId)
);

create table Rates(
	ratesId int unsigned primary key auto_increment,
	ratesType int not null default(0), check(ratesType = 0 or ratesType = 1),
	ratesName varchar(100) not null unique,
	interestRate float NOT NULL check(interestRate > 0 and interestRate < 100),
	minTerm int NOT NULL default(5),
	maxTerm int NOT NULL default (10),
	minSum float not null,
	maxSum float not null,
	constraint minMaxCheck check(maxTerm >= minTerm and minTerm >= 1 and minSum > 0 and maxSum >= minSum)
);

create table Office(
	officeId int unsigned primary key,
	phoneNumber int unsigned not null
);

create table Department(
	departmentId int unsigned primary key auto_increment,
	departmentName varchar(30) not null,
	office int unsigned,
	foreign key (office) references Office (officeId)
);

create table Employees(
	employeesId int unsigned primary key auto_increment,
	employeesSurname varchar(30) not null,
	employeesName varchar(30) not null,
	employeesPatronymic varchar(30),
	passport int unsigned not null unique,
	departmentId int unsigned,
	supervisorId int unsigned,
	foreign key (departmentId) references Department (departmentId),
	foreign key(supervisorId) references Employees(employeesId)
);

create table Scoring(
	scoringId int unsigned primary key auto_increment,
	clientsId int unsigned not null,
	employeesId int unsigned not null,
	statusScoring boolean default(false),
	foreign key (clientsId) references Clients (clientsId),
	foreign key (employeesId) references Employees (employeesId)
);

create table ApprovedTariffs(
	ApprovedTariffsId int unsigned primary key auto_increment,
    scoringId int unsigned,
    ratesId int unsigned not null,
	finishDate date,
    minSum float not null,
	maxSum float not null,
    foreign key (scoringId) references Scoring (scoringId),
	foreign key (ratesId) references Rates (ratesId)
);

create table LoansIssued(
	loansIssuedId int unsigned primary key auto_increment,
	appTarrId int unsigned not null,
    loanAmount int not null,
	startDate date not null,
	finishDate date not null,
	foreign key (AppTarrId) references ApprovedTariffs (ApprovedTariffsId)
);

create table creditsBalance(
	creditsBalanceId int unsigned primary key auto_increment,
	LoansIssuedId int unsigned not null,
    mainSum float default(0),
	percentSum float default(0),
    fineSum float default(0),
    foreign key (LoansIssuedId) references LoansIssued(loansIssuedId)
);

create table paymentSchedule(
	paymentScheduleId int unsigned primary key auto_increment,
    loansIssuedId int unsigned not null,
	deadline date not null,
	sum float not null,
    foreign key (loansIssuedId) references LoansIssued (loansIssuedId)
);

create table kindsPayments(
	kindPaymentId int unsigned primary key auto_increment,
    kindName varchar(30) not null,
    commission float not null
);

create table Payments(
	paymentsId int unsigned primary key auto_increment,
    loansIssuedId int unsigned,
	sum float not null,
    dataPayment date,
    kindPayment int unsigned,
    foreign key (loansIssuedId) references LoansIssued (loansIssuedId),
    foreign key (kindPayment) references kindsPayments (kindPaymentId)
);




