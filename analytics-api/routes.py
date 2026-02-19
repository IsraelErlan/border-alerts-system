from fastapi import APIRouter, HTTPException
import dal

router = APIRouter()

@router.get('/analytics/alerts-by-border-and-priority')
def get_alerts_by_border_and_priority(): 
    try:
        pass 
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/analytics/top-urgent-zones')
def get_top_urgent_zones():
    try:
        pass 
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/analytics/distance-distribution')
def get_distance_distribution():
    try:
        pass 
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/analytics/low-visibility-high-activity')
def get_low_visibility_high_activity():
    try:
        pass 
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/analytics/hot-zones')
def get_hot_zones():
    try:
        pass 
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))