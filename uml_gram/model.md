classDiagram
direction BT
class node18 {
    cls
   __new__(mcls, name, bases, namespace, **kwargs) 
   register(cls, subclass) 
   __instancecheck__(cls, instance) 
   __subclasscheck__(cls, subclass) 
   _dump_registry(cls, file=None) 
   _abc_registry_clear(cls) 
   _abc_caches_clear(cls) 
}
class object {
    __doc__
    __dict__
    __module__
    __annotations__
   __class__(self) 
   __class__(self, __type: type[object]) 
   __init__(self) 
   __new__(cls) 
   __setattr__(self, __name: str, __value: Any) 
   __delattr__(self, __name: str) 
   __eq__(self, __value: object) 
   __ne__(self, __value: object) 
   __str__(self) 
   __repr__(self) 
   __hash__(self) 
   __format__(self, __format_spec: str) 
   __getattribute__(self, __name: str) 
   __sizeof__(self) 
   __reduce__(self) 
   __reduce_ex__(self, __protocol: SupportsIndex) 
   __dir__(self) 
   __init_subclass__(cls) 
   __subclasshook__(cls, __subclass: type) 
}
class node20 {
   predict(self, *args, **kwargs) 
   __call__(self, *args, **kwargs) 
}
class node6 {
   fit(self, dataset: Dataset, reweighter: Reweighter) 
   predict(self, dataset: Dataset, segment: Union[Text, slice] = "test") 
}
class node13 {
   finetune(self, dataset: Dataset) 
}
class node31 {
   __call__(self, ensemble_dict: dict) 
}
class node28 {
   __call__(self, ensemble_dict: dict, *args, **kwargs) 
}
class node30 {
   __call__(self, ensemble_dict: dict) 
}
class node26 {
   __call__(self, ensemble_dict: Union[dict, object], recursion: bool = True) 
}
class node12 {
    _ens_func
    _group_func
   __init__(self, group_func=None, ens: Ensemble = None) 
   group(self, *args, **kwargs) 
   reduce(self, *args, **kwargs) 
   __call__(self, ungrouped_dict: dict, n_jobs: int = 1, verbose: int = 0, *args, **kwargs) 
}
class node21 {
   group(self, rolling_dict: dict) 
   __init__(self, ens=RollingEnsemble()) 
}
class node15 {
   get_feature_importance(self) 
}
class node33 {
    model
   __init__(self) 
   get_feature_importance(self, *args, **kwargs) 
}
class node22 {
    segments
   __init__(self, segments: Union[Dict[Text, Tuple], float], *args, **kwargs) 
   prepare_tasks(self, segments: Union[List[Text], Text], *args, **kwargs) 
   _prepare_seg(self, segment: Text) 
}
class node10 {
   fit(self, *args, **kwargs) 
   inference(self, *args, **kwargs) 
}
class node9 {
   fit(self, *args, **kwargs) 
   inference(self, *args, **kwargs) 
}
class node4 {
   fit(self, meta_dataset: MetaTaskDataset) 
   inference(self, meta_dataset: MetaTaskDataset) 
}
class node11 {
    mode
    task
    meta_info
    PROC_MODE_FULL
    PROC_MODE_TEST
    PROC_MODE_TRANSFER
   __init__(self, task: dict, meta_info: object, mode: str = PROC_MODE_FULL) 
   get_dataset(self) 
   get_meta_input(self) 
   __repr__(self) 
}
class node32 {
    nan_option
    scale_return
    assume_centered
    MASK_NAN
    FILL_NAN
    IGNORE_NAN
   __init__(self, nan_option: str = "ignore", assume_centered: bool = False, scale_return: bool = True) 
   predict(
        self,
        X: Union[pd.Series, pd.DataFrame, np.ndarray],
        return_corr: bool = False,
        is_price: bool = True,
        return_decomposed_components=False,
    ) 
   _predict(self, X: np.ndarray) 
   _preprocess(self, X: np.ndarray) 
}
class node29 {
    num_factors
    thresh
    thresh_method
    THRESH_SOFT
    THRESH_HARD
    THRESH_SCAD
   __init__(self, num_factors: int = 0, thresh: float = 1.0, thresh_method: str = "soft", **kwargs) 
   _predict(self, X: np.ndarray) 
}
class node7 {
    alpha
    target
    SHR_LW
    SHR_OAS
    TGT_CONST_VAR
    TGT_CONST_CORR
    TGT_SINGLE_FACTOR
   __init__(self, alpha: Union[str, float] = 0.0, target: Union[str, np.ndarray] = "const_var", **kwargs) 
   _predict(self, X: np.ndarray) 
   _get_shrink_target(self, X: np.ndarray, S: np.ndarray) 
   _get_shrink_target_const_var(self, X: np.ndarray, S: np.ndarray) 
   _get_shrink_target_const_corr(self, X: np.ndarray, S: np.ndarray) 
   _get_shrink_target_single_factor(self, X: np.ndarray, S: np.ndarray) 
   _get_shrink_param(self, X: np.ndarray, S: np.ndarray, F: np.ndarray) 
   _get_shrink_param_oas(self, X: np.ndarray, S: np.ndarray, F: np.ndarray) 
   _get_shrink_param_lw_const_var(self, X: np.ndarray, S: np.ndarray, F: np.ndarray) 
   _get_shrink_param_lw_const_corr(self, X: np.ndarray, S: np.ndarray, F: np.ndarray) 
   _get_shrink_param_lw_single_factor(self, X: np.ndarray, S: np.ndarray, F: np.ndarray) 
}
class node25 {
    num_factors
    solver
    FACTOR_MODEL_PCA
    FACTOR_MODEL_FA
    DEFAULT_NAN_OPTION
   __init__(self, factor_model: str = "pca", num_factors: int = 10, **kwargs) 
   _predict(self, X: np.ndarray, return_decomposed_components=False) 
}
class node17 {
    delay
    end_train_func
   __init__(
        self, experiment_name: str = None, train_func=begin_task_train, end_train_func=end_task_train, **kwargs
    ) 
   end_train(self, models, end_train_func=None, experiment_name: str = None, **kwargs) 
}
class node19 {
    delay
    skip_run_task
    end_train_func
   __init__(
        self,
        experiment_name: str = None,
        task_pool: str = None,
        train_func=begin_task_train,
        end_train_func=end_task_train,
        skip_run_task: bool = False,
        **kwargs,
    ) 
   train(self, tasks: list, train_func=None, experiment_name: str = None, **kwargs) 
   end_train(self, recs, end_train_func=None, experiment_name: str = None, **kwargs) 
   worker(self, end_train_func=None, experiment_name: str = None) 
   has_worker(self) 
}
class node1 {
    delay
   __init__(self) 
   train(self, tasks: list, *args, **kwargs) 
   end_train(self, models: list, *args, **kwargs) 
   is_delay(self) 
   __call__(self, *args, **kwargs) 
   has_worker(self) 
   worker(self) 
}
class node34 {
    _call_in_subproc
    experiment_name
    default_rec_name
    train_func
    STATUS_KEY
    STATUS_BEGIN
    STATUS_END
   __init__(
        self,
        experiment_name: Optional[str] = None,
        train_func: Callable = task_train,
        call_in_subproc: bool = False,
        default_rec_name: Optional[str] = None,
    ) 
   train(self, tasks: list, train_func: Callable = None, experiment_name: str = None, **kwargs) 
   end_train(self, models: list, **kwargs) 
}
class node8 {
    task_pool
    experiment_name
    default_rec_name
    train_func
    skip_run_task
    STATUS_KEY
    STATUS_BEGIN
    STATUS_END
    TM_ID
   __init__(
        self,
        experiment_name: str = None,
        task_pool: str = None,
        train_func=task_train,
        skip_run_task: bool = False,
        default_rec_name: Optional[str] = None,
    ) 
   train(
        self,
        tasks: list,
        train_func: Callable = None,
        experiment_name: str = None,
        before_status: str = TaskManager.STATUS_WAITING,
        after_status: str = TaskManager.STATUS_DONE,
        default_rec_name: Optional[str] = None,
        **kwargs,
    ) 
   end_train(self, recs: list, **kwargs) 
   worker(
        self,
        train_func: Callable = None,
        experiment_name: str = None,
    ) 
   has_worker(self) 
}
class node24 {
    datasets
   __init__(self, *datasets) 
   __getitem__(self, i) 
   __len__(self) 
}
class node2 {
    sampler
   __init__(self, sampler) 
   __getitem__(self, i: int) 
   __len__(self) 
}
class node3 {
    _exclude
    _dump_all
    pickle_backend
    default_dump_all
    config_attr
    exclude_attr
    include_attr
    FLAG_KEY
   __init__(self) 
   _is_kept(self, key) 
   __getstate__(self) 
   __setstate__(self, state: dict) 
   dump_all(self) 
   _get_attr_list(self, attr_type: str) 
   config(self, recursive=False, **kwargs) 
   to_pickle(self, path: Union[Path, str], **kwargs) 
   load(cls, filepath) 
   get_backend(cls) 
   general_dump(obj, path: Union[Path, str]) 
}
class node0 {
   __getitem__(self, index) 
   __add__(self, other: "Dataset[T_co]") 
}
class node14 {
   __hash__(self) 
}
class node23 {
   __iter__(self) 
}
class node5 {
   __next__(self) 
   __iter__(self) 
}
class node16 {
   __len__(self) 
}

node14  ..>  object 
node18 "isinstanceof" ..>  node20 
node3  -->  node20 
node20  -->  node6 
node6  -->  node13 
node28  -->  node31 
object  -->  node28 
node28  -->  node30 
node28  -->  node26 
object  -->  node12 
node12  -->  node21 
object  -->  node15 
node15  -->  node33 
node18 "isinstanceof" ..>  node22 
node3  -->  node22 
node9  -->  node10 
node18 "isinstanceof" ..>  node9 
object  -->  node9 
node9  -->  node4 
object  -->  node11 
node20  -->  node32 
node32  -->  node29 
node32  -->  node7 
node32  -->  node25 
node34  -->  node17 
node8  -->  node19 
object  -->  node1 
node1  -->  node34 
node1  -->  node8 
node0  -->  node24 
node23  ..>  node24 
node5  ..>  node24 
node16  ..>  node24 
object  -->  node2 
node23  ..>  node2 
node5  ..>  node2 
node16  ..>  node2 
object  -->  node3 
object  -->  node0 
node23  ..>  node0 
node5  ..>  node0 
