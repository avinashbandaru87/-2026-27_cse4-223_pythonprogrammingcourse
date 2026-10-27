The University Scholarship Allocation System is designed to automate the selection of students eligible for university scholarships based on academic performance, subject-wise minimum marks, attendance percentage, and annual family income.

The system accepts the applicant's ID, name, marks in each subject, attendance percentage, and annual family income. It calculates the aggregate percentage and checks whether the applicant satisfies all eligibility criteria.

Students who meet all the requirements are ranked in descending order of aggregate marks. In case of a tie, the system considers higher attendance, higher total subject marks, and finally lower application ID. Students who do not qualify are displayed along with their reasons for rejection.

Eligibility criteria used in this project:
- Aggregate marks: at least 75%.
- Subject-wise marks: at least 40 out of 100 in every subject.
- Attendance: at least 75%.
- Annual family income: not more than ₹2,50,000.
These are example criteria and can be changed to match actual university scholarship rules.
2. Algorithm
3. Start the program.
4. Read the number of scholarship applicants.
5. For each applicant, input the application ID, name, subject marks, attendance, and annual family income.
6. Calculate the total marks and aggregate percentage.
7. Check whether the aggregate is at least 75%.
8. Check whether every subject mark is at least 40.
9. Check whether attendance is at least 75%.
10. Check whether annual family income is at most ₹2,50,000.
11. If all conditions are satisfied, classify the applicant as eligible; otherwise, record the rejection reasons.
12. Sort eligible applicants using the following priority:
    - Higher aggregate percentage.
    - Higher attendance percentage.
    - Higher total marks.
    - Lower application ID.
11. Display the ranked merit list and ineligible applicants with rejection reasons.
12. Stop.
###3. Flowchart

```Mermaid
flowchart TD
    A([Start]) --> B[/Input number of applicants/]
    B --> C[/Input student details and marks/]
    C --> D[Calculate aggregate percentage]
    D --> E{Aggregate >= 75%?}
    E -- No --> R[Record rejection reason]
    E -- Yes --> F{All subjects >= 40?}
    F -- No --> R
    F -- Yes --> G{Attendance >= 75%?}
    G -- No --> R
    G -- Yes --> H{Income <= Rs. 250000?}
    H -- No --> R
    H -- Yes --> I[Add to eligible list]
    R --> J{More applicants?}
    I --> J
    J -- Yes --> C
    J -- No --> K[Sort eligible applicants]
    K --> L[Apply tie-breaking rules]
    L --> M[/Display ranked merit list/]
    M --> N[/Display rejection reasons/]
    N --> O([Stop])
 ```


###5. Sample Input
Enter the following details when running the Python program.

Enter number of applicants: 3

Applicant 1
Application ID: 101
Student name: Ravi
Number of subjects: 3
Marks for subject 1: 85
Marks for subject 2: 80
Marks for subject 3: 90
Attendance percentage: 90
Annual family income (Rs.): 200000

Applicant 2
Application ID: 102
Student name: Priya
Number of subjects: 3
Marks for subject 1: 80
Marks for subject 2: 80
Marks for subject 3: 80
Attendance percentage: 95
Annual family income (Rs.): 220000

Applicant 3
Application ID: 103
Student name: Kumar
Number of subjects: 3
Marks for subject 1: 90
Marks for subject 2: 30
Marks for subject 3: 85
Attendance percentage: 90
Annual family income (Rs.): 180000



###6. Sample Output

===== SCHOLARSHIP MERIT LIST =====
Rank 1: ID=101, Name=Ravi, Aggregate=85.00%, Attendance=90.00%
Rank 2: ID=102, Name=Priya, Aggregate=80.00%, Attendance=95.00%

===== INELIGIBLE APPLICANTS =====
ID=103, Name=Kumar
Reasons: Aggregate marks below 75%,
         Subject-wise minimum marks not met



Explanation:
- Ravi is ranked first because his aggregate is 85%.
- Priya is ranked second because her aggregate is 80%.
- Kumar is ineligible because his aggregate is below 75% and one subject mark is below 40.
###7. Mermaid Flowchart Code
Copy this code into the Mermaid Live Editor to view or export the flowchart.
#chatgpt-mermaid-_r_el_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_el_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_el_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_el_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-_r_el_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_el_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_el_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_el_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_el_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_el_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_el_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_el_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_el_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_el_ p{margin:0;}#chatgpt-mermaid-_r_el_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_el_ .label text,#chatgpt-mermaid-_r_el_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ .node rect,#chatgpt-mermaid-_r_el_ .node circle,#chatgpt-mermaid-_r_el_ .node ellipse,#chatgpt-mermaid-_r_el_ .node polygon,#chatgpt-mermaid-_r_el_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-_r_el_ .rough-node .label text,#chatgpt-mermaid-_r_el_ .node .label text,#chatgpt-mermaid-_r_el_ .image-shape .label,#chatgpt-mermaid-_r_el_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_el_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_el_ .rough-node .label,#chatgpt-mermaid-_r_el_ .node .label,#chatgpt-mermaid-_r_el_ .image-shape .label,#chatgpt-mermaid-_r_el_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_el_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_el_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_el_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-_r_el_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-_r_el_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-_r_el_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_el_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-_r_el_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_el_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-_r_el_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-_r_el_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_el_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-_r_el_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_el_ .icon-shape,#chatgpt-mermaid-_r_el_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-_r_el_ .icon-shape p,#chatgpt-mermaid-_r_el_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-_r_el_ .icon-shape .label rect,#chatgpt-mermaid-_r_el_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-_r_el_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_el_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_el_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-_r_el_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_el_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_el_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_el_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_el_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_el_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_el_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_el_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_el_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-_r_el_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_el_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_el_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_el_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_el_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_el_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_el_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_el_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_el_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-_r_el_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_el_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_el_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-_r_el_ .node rect,#chatgpt-mermaid-_r_el_ .node circle,#chatgpt-mermaid-_r_el_ .node ellipse,#chatgpt-mermaid-_r_el_ .node polygon,#chatgpt-mermaid-_r_el_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_el_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_el_ .node.mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_el_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_el_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-_r_el_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of applicantsInput student details andmarksCalculate aggregatepercentageAggregate = 75%?Record rejection reasonAll subjects = 40?Attendance = 75%?Income <= Rs. 250000?Add to eligible listMore applicants?Sort eligible applicantsApply tie-breaking rulesDisplay ranked merit listDisplay rejection reasonsStopNoYesNoYesNoYesNoYesYesNo





###8. Tie-Breaking Rules
Priority	Condition
1	Higher aggregate percentage
2	Higher attendance percentage
3	Higher total subject marks
4	Lower application ID

These rules ensure that students with identical aggregate marks are ranked consistently.
###9. Conclusion
The University Scholarship Allocation System automates scholarship eligibility verification and merit ranking. It considers academic performance, subject-wise minimum scores, attendance, and family income. It also resolves ties using predefined rules and explains why applicants are rejected.

Programming language: Python 3

Concepts used: Functions, lists, dictionaries, loops, conditional statements, sorting, and Mermaid flowcharts.
