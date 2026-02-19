from fastapi import APIRouter, HTTPException
import dal

router = APIRouter()

@router.get('/analytics/alerts-by-border-and-priority')
def get_alerts_by_border_and_priority(): 
    try:
        dal.get_alerts_by_border_and_priority()
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/analytics/top-urgent-zones')
def get_top_urgent_zones():
    try:
        dal.get_top_urgent_zones()
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/analytics/distance-distribution')
def get_distance_distribution():
    try:
        dal.get_distance_distribution()
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/analytics/low-visibility-high-activity')
def get_low_visibility_high_activity():
    try:
        dal.get_low_visibility_high_activity()
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/analytics/hot-zones')
def get_hot_zones():
    try:
        dal.get_hot_zones()
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))