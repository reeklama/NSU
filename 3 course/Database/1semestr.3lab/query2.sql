set @startPeriod  := 20190601;
set @finishPeriod  := 20200101;

select round(psum / tsum, 4) as income
from (
	(select Payments.loansIssuedId, sum(sum) as psum
	from Payments inner join LoansIssued on Payments.loansIssuedId = LoansIssued.loansIssuedId
	where LoansIssued.startDate between @startPeriod and @finishPeriod) as first 
    left join 
    (select LoansIssued.loansIssuedId, sum(loanAmount) as tsum
	from LoansIssued
	where LoansIssued.startDate between @startPeriod and @finishPeriod) as second 
    on first.loansIssuedId = second.loansIssuedId
    )