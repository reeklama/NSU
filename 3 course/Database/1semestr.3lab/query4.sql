set @startPeriod := 20180101;
set @finishPeriod := 20200101;


select distinct
	t1.ratesId,
	t1.ratesName,
    	SUM(t2.loanAmount) OVER () as sumAmount,
	COUNT(t2.loanAmount) OVER () as countAmount,
	AVG(t2.loanAmount) OVER (PARTITION BY t1.ratesId) as avgAmount,
	FIRST_VALUE(t2.clientsId) OVER (PARTITION BY t1.ratesId ORDER BY loanAmount DESC) as maxLoanClientId
from
	(Rates t1 inner join 
    (select LoansIssued.loansIssuedId, ApprovedTariffs.ratesId, LoansIssued.loanAmount, Scoring.clientsId
	from LoansIssued inner join (ApprovedTariffs left join Scoring on ApprovedTariffs.scoringId = Scoring.scoringId) on LoansIssued.appTarrId = ApprovedTariffs.ApprovedTariffsId
	where LoansIssued.startDate between @startPeriod and @finishPeriod) as t2
     on t1.ratesId = t2.ratesId)