export class ExperimentModel {
	public uuid: string;
	public unique_name: string;
	public sequence: number;
	public experiment_group_name: string;
	public user: string;
	public content: string;
	public num_jobs: number;
	public last_status: string;
	public project_name: string;
	public experiment_group: string;
	public deleted?: boolean;
	public project?: string;
	public status?: string;
	public createdAt: Date;
	public updatedAt: Date;
	public started_at: Date;
	public finished_at: Date;
}

export class ExperimentStateSchema {
	byUuids: {[uuid: string]: ExperimentModel};
	uuids: string[];
}

export const ExperimentsEmptyState = {byUuids: {}, uuids: []};