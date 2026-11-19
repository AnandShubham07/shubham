# Write your MySQL query statement below
select s.student_id,s.student_name,ss.subject_name, Count(e.subject_name) as attended_exams 
    from( Subjects ss join Students s ) 
            left join Examinations e 
            on e.student_id=s.student_id 
            and ss.subject_name=e.subject_name

            group by s.student_id,s.student_name,ss.subject_name 
            order by s.student_id,ss.subject_name
;