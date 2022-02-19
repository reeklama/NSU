set @startPeriod := 20190601;
set @finishPeriod := 20200101;

select 
	selectedCredits.loansIssuedId,
    round( sum(Payments.sum) / selectedCredits.loanAmount, 3) as income
from (
	(select loansIssuedId, startDate, finishDate, loanAmount
	from LoansIssued
	where startDate between @startPeriod and @finishPeriod) as selectedCredits
    left join Payments
    on selectedCredits.loansIssuedId = Payments.loansIssuedId and Payments.dataPayment between selectedCredits.startDate and DATE_ADD(selectedCredits.finishDate, interval '2' month)
) 
group by selectedCredits.loansIssuedId, selectedCredits.loanAmount

