set @startPeriod  := 20190601;
set @finishPeriod  := 20200101;

select year(dataPayment) as year,  
	month(dataPayment) as month, 
    day(dataPayment) as day, 
    round(sum(sum), 0) as sum, 
    count(sum) as num
from Payments inner join LoansIssued on Payments.loansIssuedId = LoansIssued.loansIssuedId
where LoansIssued.startDate between @startPeriod  and  @finishPeriod
group by year(dataPayment), month(dataPayment), day(dataPayment) with rollup