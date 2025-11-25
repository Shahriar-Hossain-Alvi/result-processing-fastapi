# from sqlalchemy import select, join, and_

# async def get_offered_subjects_for_marking(
#     db: AsyncSession, 
#     target_semester_id: int, 
#     target_department_id: int
# ):
#     # Ensure you import Subject and SubjectOfferings models
    
#     # 1. Define the join
#     j = join(Subject, 
#              SubjectOfferings, 
#              Subject.id == SubjectOfferings.subject_id)

#     # 2. Build the statement
#     statement = select(Subject).select_from(j).where(
#         and_(
#             Subject.semester_id == target_semester_id,
#             SubjectOfferings.department_id == target_department_id
#         )
#     )

#     # 3. Execute and fetch all results
#     result = await db.execute(statement)
    
#     # Use result.scalars().all() to get a list of Subject objects
#     return result.scalars().all()